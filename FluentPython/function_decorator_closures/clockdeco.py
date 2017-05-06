#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
import functools

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        @functools.wraps(func)
        def clocked(*args):
            t0 = time.perf_counter()
            result = func(*args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in args)
            result = repr(result)
            print(fmt.format(**locals()))
            return result

        return clocked

    return decorate
