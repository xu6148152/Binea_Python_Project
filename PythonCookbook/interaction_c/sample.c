/* sample.c */
//#include <math.h>
//#include "sample.h"
///* Compute the greatest common divisor */
//int gcd(int x, int y) {
//    int g = y;
//    while (x > 0) {
//        g = x;
//        x = y % x;
//        y = g;
//    }
//    return g;
//}
//
///* Test if (x0,y0) is in the Mandelbrot set or not */
//int in_mandel(double x0, double y0, int n) {
//    double x=0,y=0,xtemp;
//    while (n > 0) {
//        xtemp = x*x - y*y + x0;
//        y = 2*x*y + y0;
//        x = xtemp;
//        n -= 1;
//        if (x*x + y*y > 4) return 0;
//    }
//    return 1;
//}
//
///* Divide two numbers */
//int divide(int a, int b, int *remainder) {
//    int quot = a / b;
//    *remainder = a % b;
//    return quot;
//}
//
///* Average values in an array */
//double avg(double *a, int n) {
//    int i;
//    double total = 0.0;
//    for (i = 0; i < n; i++) {
//        total += a[i];
//    }
//    return total / n;
//}
//
///* A C data structure */
////typedef struct Point {
////    double x,y;
////} Point;
//
///* Function involving a C data structure */
//double distance(Point *p1, Point *p2) {
//    return hypot(p1->x - p2->x, p1->y - p2->y);
//}





#include "Python.h"
#include "sample.h"

/* int gcd(int, int) */
static PyObject *py_gcd(PyObject *self, PyObject *args) {
  int x, y, result;

  if (!PyArg_ParseTuple(args,"ii", &x, &y)) {
    return NULL;
  }
  result = gcd(x,y);
  return Py_BuildValue("i", result);
}

/* int in_mandel(double, double, int) */
static PyObject *py_in_mandel(PyObject *self, PyObject *args) {
  double x0, y0;
  int n;
  int result;

  if (!PyArg_ParseTuple(args, "ddi", &x0, &y0, &n)) {
    return NULL;
  }
  result = in_mandel(x0,y0,n);
  return Py_BuildValue("i", result);
}

/* int divide(int, int, int *) */
static PyObject *py_divide(PyObject *self, PyObject *args) {
  int a, b, quotient, remainder;
  if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
    return NULL;
  }
  quotient = divide(a,b, &remainder);
  return Py_BuildValue("(ii)", quotient, remainder);
}

/* Module method table */
static PyMethodDef SampleMethods[] = {
  {"gcd",  py_gcd, METH_VARARGS, "Greatest common divisor"},
  {"in_mandel", py_in_mandel, METH_VARARGS, "Mandelbrot test"},
  {"divide", py_divide, METH_VARARGS, "Integer division"},
  { NULL, NULL, 0, NULL}
};

/* Module structure */
static struct PyModuleDef samplemodule = {
  PyModuleDef_HEAD_INIT,

  "sample",           /* name of module */
  "A sample module",  /* Doc string (may be NULL) */
  -1,                 /* Size of per-interpreter state or -1 */
  SampleMethods       /* Method table */
};

/* Module initialization function */
PyMODINIT_FUNC
PyInit_sample(void) {
  return PyModule_Create(&samplemodule);
}