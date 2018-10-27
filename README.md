# Homework 12

### Build cython
python setup.py build_ext --inplace

### Build c extension 
python setup_c_ext.py build_ext --inplace

#### Timings to generate 1000-th fibonacci number
* **python**: 0.00012183189392089844 ms
* **CPython**: 4.38690185546875e-05 ms
* **C++ extension**: 6.9141387939453125e-06 ms