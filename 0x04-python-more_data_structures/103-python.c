#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p) {
    printf("[*] Python list info\n");

    if (PyList_Check(p)) {
        printf("[*] Size of the Python List = %ld\n", PyList_Size(p));

        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
        
        for (Py_ssize_t i = 0; i < PyList_Size(p); ++i) {
            PyObject *item = PyList_GET_ITEM(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        }
    } else {
        fprintf(stderr, "  [ERROR] Invalid List Object\n");
    }
}

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p) {
    printf("[.] bytes object info\n");

    if (PyBytes_Check(p)) {
        printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
        printf("  trying string: %s\n", PyBytes_AS_STRING(p));

        printf("  first %ld bytes: ", ((PyVarObject *)p)->ob_size + 1);

        for (Py_ssize_t i = 0; i <= ((PyVarObject *)p)->ob_size && i < 10; ++i) {
            printf("%02hhx", ((char *)p)[i]);
            if (i < ((PyVarObject *)p)->ob_size) {
                printf(" ");
            }
        }

        printf("\n");
    } else {
        fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
    }
}
