"""
    Homework 2 of Advanced Python course.
    Task: Write a script that cause a Segmentation Fault error.
    I claim that I used a materials form here
    https://wiki.python.org/moin/CrashingPython
"""

import ctypes
import sys


def crash_with_recursion():
    """Python interpreter can be crushed by resource exhaustion."""

    sys.setrecursionlimit(2**30)

    def func(func):
        func(func)

    func(func)


def crash_with_ctypes():
    """Crash the Python interpreter with ctypes."""

    i = ctypes.c_char('a')
    j = ctypes.pointer(i)
    c = 0
    while True:
        j[c] = 'a'
        c += 1
        j


if __name__ == '__main__':
    crash_with_recursion()
    # crash_with_ctypes()
