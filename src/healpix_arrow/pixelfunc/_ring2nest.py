import healpy as hp

import pyarrow as pa
import pyarrow.compute as pc


function_name = "ring2nest"
function_docs = {
    "summary": "wrapper for healpy.pixelfunc.ring2nest",
    "description": hp.ring2nest.__doc__,
}

input_types = {
   "nside" : pa.int64(),
   "ipix" : pa.int64(),
}
output_type = pa.int64()


def ring2nest_wrapper(ctx, nside, ipix_ring):
    if isinstance(nside, pa.Scalar):
        nside = nside.as_py()
    if isinstance(ipix_ring, pa.Scalar):
        ipix_ring = ipix_ring.as_py()
    ipix_nest = hp.ring2nest(nside, ipix_ring)
    return pa.array(ipix_nest)


pc.register_scalar_function(
    ring2nest_wrapper,
    function_name,
    function_docs,
    input_types,
    output_type,
)
