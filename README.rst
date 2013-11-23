2D and 3D phase unwrapping
==========================

This is a Python wrapper for 2D and 3D phase unwrapping code based on:

* (2D) M. A. Herráez, D. R. Burton, M. J. Lalor, and M. A. Gdeisat, "Fast two-dimensional phase-unwrapping algorithm based on sorting by reliability following a noncontinuous path", `Applied Optics, Vol. 41, Issue 35, pp. 7437-7444 (2002) <http://dx.doi.org/10.1364/AO.41.007437>`_,
* (3D) H. Abdul-Rahman, M. Gdeisat, D. Burton, M. Lalor, "Fast three-dimensional phase-unwrapping algorithm based on sorting by reliability following a non-continuous path", `Proc. SPIE 5856, Optical Measurement Systems for Industrial Inspection IV, 32 (2005) <http://dx.doi.ogr/doi:10.1117/12.611415>`_.

More information about the code can be found on GERI homepage: `2D <http://www.ljmu.ac.uk/GERI/90207.htm>`_, `3D <http://www.ljmu.ac.uk/GERI/90208.htm>`_.
The general principle and applications are the same as those for a 1D ``unwrap`` `available in numpy <http://docs.scipy.org/doc/numpy/reference/generated/numpy.unwrap.html>`_.


Usage
-----

The package is based on `cffi <https://pypi.python.org/pypi/cffi>`_ and requires it for installation:

::

    $ pip install cffi
    $ pip install unwrap

The interface consists of a single function:

::

    >>> from unwrap import unwrap
    >>> unwrap(
    ...    wrapped_array,
    ...    wrap_around_axis_0=False,
    ...    wrap_around_axis_1=False,
    ...    wrap_around_axis_2=False)

It takes a 2- or 3-dimensional ``numpy`` array of floats and returns an array with the same shape with the values changed by ``(2 pi n)`` such that the whole array has the least amount of jumps.
Usage examples can be found in ``test/test_unwrap.py``.
