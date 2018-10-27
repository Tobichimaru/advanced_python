from Cython.Distutils import build_ext
from distutils.core import setup
from distutils.extension import Extension


setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[
        Extension("c_fibonacci", ["c_fibonacci.pyx"])
    ]
)
