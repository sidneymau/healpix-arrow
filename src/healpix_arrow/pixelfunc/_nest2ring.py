import healpy as hp

import pyarrow as pa
import pyarrow.compute as pc


function_name = "nest2ring"
function_docs = {
    "summary": "wrapper for healpy.pixelfunc.nest2ring",
    "description": hp.nest2ring.__doc__,
}

input_types = {
   "nside" : pa.int64(),
   "ipix" : pa.int64(),
}
output_type = pa.int64()


def nest2ring_wrapper(ctx, nside, ipix_nest):
    if isinstance(nside, pa.Scalar):
        nside = nside.as_py()
    if isinstance(ipix_nest, pa.Scalar):
        ipix_nest = ipix_nest.as_py()
    ipix_ring = hp.nest2ring(nside, ipix_nest)
    return pa.array(ipix_ring)


pc.register_scalar_function(
    nest2ring_wrapper,
    function_name,
    function_docs,
    input_types,
    output_type,
)
