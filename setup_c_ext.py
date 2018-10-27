from distutils.core import setup
from distutils.extension import Extension


setup(
    name='fibonacci',
    ext_modules=[
        Extension('fibonacci', ['c_ext_fibonacci.c']),
    ]
)
