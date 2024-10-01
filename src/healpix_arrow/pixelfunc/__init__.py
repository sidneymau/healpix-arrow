import pyarrow.compute as pc

from . import _ang2pix
from . import _pix2ang
from . import _nest2ring
from . import _ring2nest


def ang2pix(nside, ra, dec):
    return pc.field("")._call("ang2pix", [nside, ra, dec])


def pix2ang(nside, ipix):
    return pc.field("")._call("pix2ang", [nside, ipix])


def nest2ring(nside, ipix):
    return pc.field("")._call("nest2ring", [nside, ipix])


def ring2nest(nside, ipix):
    return pc.field("")._call("ring2nest", [nside, ipix])
