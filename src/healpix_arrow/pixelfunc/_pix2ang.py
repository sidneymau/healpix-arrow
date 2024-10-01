import healpy as hp

import pyarrow as pa
import pyarrow.compute as pc


function_name = "pix2ang"
function_docs = {
    "summary": "wrapper for healpy.pixelfunc.pix2ang",
    "description": hp.pix2ang.__doc__,
}

input_types = {
   "nside" : pa.int64(),
   "ipix" : pa.int64(),
}
# TODO would a list output be more appropriate?
output_type = pa.struct(
    [
        ("theta", pa.float64()),
        ("phi", pa.float64()),
    ]
)


def pix2ang_wrapper(ctx, nside, ipix):
    if isinstance(nside, pa.Scalar):
        nside = nside.as_py()
    if isinstance(ipix, pa.Scalar):
        ipix = ipix.as_py()
    theta, phi = hp.pix2ang(nside, ipix, lonlat=True)
    return pa.StructArray.from_arrays(
        (pa.array(theta), pa.array(phi)),
        names=("theta", "phi"),
    )


pc.register_scalar_function(
    pix2ang_wrapper,
    function_name,
    function_docs,
    input_types,
    output_type,
)
