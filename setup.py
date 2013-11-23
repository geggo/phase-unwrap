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


DOCUMENTATION = open('README.rst').read()

setup(
    name='unwrap',
    version="0.1.0",
    author='Gregor Thalhammer',
    author_email='gregor.thalhammer@gmail.com',
    url='http://github.com/geggo/phase-unwrap',
    description='2D and 3D phase unwrapping',
    long_description=DOCUMENTATION,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Operating System :: OS Independent'
        ],
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
