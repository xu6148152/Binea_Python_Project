#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import numpy as np
from numpy.matlib import randn

data1 = [6, 7.5, 8, 0, 1]
arr = np.arange(10)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [7, 8, 9], [10, 11, 12]])


def test_np_type():
    arr1 = np.array(data1)
    print(arr1.dtype)


def test_np_arr():
    print(arr)


def test_index_slice():
    # print(arr[1:6])
    # print(arr2d[:2, 1:])
    # print(arr2d[1, :2])
    print(arr2d[:, :1])


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

data = randn(7, 4)

arr = np.empty((8, 4))


def test_boolean_index():
    # print(names)
    # print(data)
    print(names == 'Bob')
    print(data[names == 'Bob', 2:])


def test_fancy_index():
    for i in range(8):
        arr[i] = i

    # print(arr)

    # print(arr[[4, 3, 0, 6]])
    print(arr[[-2, -3, -7]])


def test_transpose():
    arr = np.arange(15).reshape((3, 5))
    print(arr)
    print(arr.T)


def test_ufunc():
    arr = np.arange(10)
    print(np.sqrt(arr))


def test_meshgrid():
    points = np.arange(-5, 5, 0.01)
    xs, ys = np.meshgrid(points, points)
    print(ys)


def test_where():
    arr = randn(4, 4)
    print(np.where(arr > 0, 2, -2))
    print(np.where(arr > 0, 2, arr))


def test_linalg():
    from numpy.linalg import inv, qr
    X = randn(5, 5)
    mat = X.T.dot(X)
    print(inv(mat))
    print(mat.dot(inv(mat)))


def test_random_walk():
    import random
    position = 0
    walk = [position]
    steps = 1000
    for i in range(steps):
        step = 1 if random.randint(0, 1) else -1
        position += step
        walk.append(position)
    print(walk)


if __name__ == '__main__':
    test_random_walk()
