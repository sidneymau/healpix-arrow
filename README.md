# healpix-arrow

Wrappers for calling HEALPix routines (via [healpy](https://healpy.readthedocs.io/en/latest/index.html)) in pyarrow.
Currently, only a small subset of pixelisation-related routines are supported.

---

Use of the HEALPix/healpy software package should be explicitly acknowledged in all publications in the following form:

* an acknowledgment statement – "Some of the results in this paper have been derived using the healpy and HEALPix package"
* at the first use of the HEALPix acronym, a footnote placed in the main body of the paper referring to the HEALPix website – currently http://healpix.sourceforge.net

BibTeX record:
```
@article{Zonca2019,
  doi = {10.21105/joss.01298},
  url = {https://doi.org/10.21105/joss.01298},
  year = {2019},
  month = mar,
  publisher = {The Open Journal},
  volume = {4},
  number = {35},
  pages = {1298},
  author = {Andrea Zonca and Leo Singer and Daniel Lenz and Martin Reinecke and Cyrille Rosset and Eric Hivon and Krzysztof Gorski},
  title = {healpy: equal area pixelization and spherical harmonics transforms for data on the sphere in Python},
  journal = {Journal of Open Source Software}
}
```
```
@ARTICLE{2005ApJ...622..759G,
   author = {{G{\'o}rski}, K.~M. and {Hivon}, E. and {Banday}, A.~J. and 
	{Wandelt}, B.~D. and {Hansen}, F.~K. and {Reinecke}, M. and 
	{Bartelmann}, M.},
    title = "{HEALPix: A Framework for High-Resolution Discretization and Fast Analysis of Data Distributed on the Sphere}",
  journal = {\apj},
   eprint = {arXiv:astro-ph/0409513},
 keywords = {Cosmology: Cosmic Microwave Background, Cosmology: Observations, Methods: Statistical},
     year = 2005,
    month = apr,
   volume = 622,
    pages = {759-771},
      doi = {10.1086/427976},
   adsurl = {http://adsabs.harvard.edu/abs/2005ApJ...622..759G},
  adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```
