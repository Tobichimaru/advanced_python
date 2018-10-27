import time

import c_fibonacci
import fibonacci as c_ext_fibonacci
import py_fibonacci


def timeit(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        print(t2 - t1)
        return res
    return wrapper


@timeit
def test_pyx_fibonacci():
    print("pyx fib")
    c_fibonacci.get_fibonacci(1000)


@timeit
def test_py_fibonacci():
    print("py fib")
    py_fibonacci.get_fibonacci(1000)


@timeit
def test_c_ext_fibonacci():
    print("c ext fib")
    c_ext_fibonacci.fibonacci(1000)


if __name__ == "__main__":
    test_py_fibonacci()
    test_pyx_fibonacci()
    test_c_ext_fibonacci()
