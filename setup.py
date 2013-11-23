import sys
from setuptools import setup, Extension


# FIXME: for the time being bootstrapping is not possible.
# Look into it again when CFFI 1.0 is released.
try:
    import cffi
except ImportError:
    sys.stderr.write('Error: CFFI (required for setup) is not available.\n')
    sys.stderr.write('Please use "pip install cffi", or equivalent.\n')
    sys.exit(1)


import unwrap.unwrap2D as unwrap2D
import unwrap.unwrap3D as unwrap3D

setup(
    name='unwrap',
    version="0.1.0",
    install_requires=[
        "numpy>=1.6",
        "cffi>=0.7",
        ],
    package_data={'unwrap': ['*.c']},
    packages=['unwrap'],
    provides=['unwrap'],
    ext_package="unwrap",
    ext_modules=[
        unwrap2D._ffi.verifier.get_extension(),
        unwrap3D._ffi.verifier.get_extension()
        ],
    zip_safe=False, # cffi requirement for setuptools
    )
