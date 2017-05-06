#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from dis import dis

b = 6


def f1(a):
    # global b
    print(a)
    print(b)
    b = 9


if __name__ == '__main__':
    dis(f1)
