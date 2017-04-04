#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import timeit


def clock(label, cmd, setup, times):
    res = timeit.repeat(cmd, setup=setup, number=times)
    print(label, *('{:.3f}'.format(x) for x in res))
