#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from function_decorator_closures.clockdeco import clock
import functools


@functools.lru_cache()
@clock
def fibonacci(n):
    return n if n < 2 else fibonacci(n - 2) * fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(6))
