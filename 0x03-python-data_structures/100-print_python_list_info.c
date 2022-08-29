#include <Python.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: PyObject list
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int size, mem, i;
	PyObject *obj;

	size = Py_SIZE(p);
	mem = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
