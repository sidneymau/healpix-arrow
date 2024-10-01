import healpy as hp

import pyarrow as pa
import pyarrow.compute as pc


function_name = "ang2pix"
function_docs = {
    "summary": "wrapper for healpy.pixelfunc.ang2pix",
    "description": hp.ang2pix.__doc__,
}

input_types = {
   "nside" : pa.int64(),
   "theta" : pa.float64(),
   "phi" : pa.float64(),
   "nest": pa.bool_(),
   "lonlat": pa.bool_(),
}
output_type = pa.int64()


def ang2pix_wrapper(ctx, nside, theta, phi, nest, lonlat):
    if isinstance(nside, pa.Scalar):
        nside = nside.as_py()
    if isinstance(theta, pa.Scalar):
        theta = nside.as_py()
    if isinstance(phi, pa.Scalar):
        phi = nside.as_py()
    ipix = hp.ang2pix(nside, theta, phi, nest=nest, lonlat=lonlat)
    return pa.array(ipix)


pc.register_scalar_function(
    ang2pix_wrapper,
    function_name,
    function_docs,
    input_types,
    output_type,
)
