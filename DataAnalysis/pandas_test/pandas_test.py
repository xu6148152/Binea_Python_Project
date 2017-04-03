#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from pandas import Series, DataFrame


def test_series():
    obj = Series([4, 7, -5, 3])
    print(obj)
    print(obj.values)
    print(obj.index)

    obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
    print(obj2)
    print(obj2.index)


def test_dataframe():
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    frame = DataFrame(data)
    print(frame)
    frame['eastern'] = frame.state == 'Ohio'
    print(frame)
    del frame['eastern']
    print(frame)

if __name__ == '__main__':
    test_dataframe()
