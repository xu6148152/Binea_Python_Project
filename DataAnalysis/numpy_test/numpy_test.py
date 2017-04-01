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

if __name__ == '__main__':
    test_fancy_index()
