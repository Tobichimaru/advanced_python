#include <Python.h>


long long fibonacci(unsigned int n) {
    if (n < 1) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    long long prev = 0;
    long long prev_prev = 1;
    long long curr = 0;
    for (unsigned int i = 0; i < n; ++i) {
        curr = prev + prev_prev;
        prev_prev = prev;
        prev = curr;
    }
    return curr;
}


static PyObject* fibonacci_py(PyObject* self, PyObject* args) {
    PyObject *result = NULL;
    long n;
    long long fib;
    if (PyArg_ParseTuple(args, "l", &n)) {
        fib = fibonacci(n);
        result = Py_BuildValue("L", fib);
    }
    return result;
}


static PyMethodDef fibonacci_module_methods[] = {
    {"fibonacci", (PyCFunction)fibonacci_py, METH_VARARGS},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef fibonacci_module_definition = {
    PyModuleDef_HEAD_INIT,
    "fibonacci",
    "Extension module that provides fibonacci sequence function",
    -1,
    fibonacci_module_methods
};


PyMODINIT_FUNC PyInit_fibonacci(void) {
    Py_Initialize();

    return PyModule_Create(&fibonacci_module_definition);
}
