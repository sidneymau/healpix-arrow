import pyarrow.compute as pc

from . import _ang2pix
from . import _pix2ang
from . import _nest2ring
from . import _ring2nest


def ang2pix(nside, ra, dec, nest=False, lonlat=False):
    return pc.field("")._call("ang2pix", [nside, ra, dec, nest, lonlat])


def pix2ang(nside, ipix, nest=False, lonlat=False):
    return pc.field("")._call("pix2ang", [nside, ipix, nest, lonlat])


def nest2ring(nside, ipix):
    return pc.field("")._call("nest2ring", [nside, ipix])


def ring2nest(nside, ipix):
    return pc.field("")._call("ring2nest", [nside, ipix])
