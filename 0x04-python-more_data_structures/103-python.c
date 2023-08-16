#include <Python.h>

/**
 * print_python_list - Prints basic information about a Python list object.
 * @p: The PyObject representing the Python list.
 */
void print_python_list(PyObject *p) {
    printf("[*] Python list info\n");

    if (PyList_Check(p)) {
        Py_ssize_t size = PyList_Size(p);
        printf("[*] Size of the Python List = %ld\n", size);

        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

        for (Py_ssize_t i = 0; i < size; ++i) {
            PyObject *item = PyList_GET_ITEM(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        }
    } else {
        fprintf(stderr, "  [ERROR] Invalid List Object\n");
    }
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object.
 * @p: The PyObject representing the Python bytes object.
 */
void print_python_bytes(PyObject *p) {
    printf("[.] bytes object info\n");

    if (PyBytes_Check(p)) {
        Py_ssize_t size = ((PyVarObject *)p)->ob_size;
        printf("  size: %ld\n", size);

        printf("  trying string: %s\n", PyBytes_AS_STRING(p));

        printf("  first %ld bytes: ", size + 1);

        for (Py_ssize_t i = 0; i <= size && i < 10; ++i) {
            printf("%02hhx", ((char *)p)[i]);
            if (i < size) {
                printf(" ");
            }
        }

        printf("\n");
    } else {
        fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
    }
}
