#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from inspect import getgeneratorstate
from functools import wraps
from collections import namedtuple

Result = namedtuple('Result', 'count average')


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)


def simple_coro2(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)


def coroutine(func):
    """Decorator: primes 'func' by advancing to first 'yield'"""

    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


def test_coroutine():
    # my_coro = simple_coroutine()
    # print(my_coro)
    # print(inspect.getgeneratorstate(my_coro))
    # next(my_coro)
    # print(inspect.getgeneratorstate(my_coro))
    # my_coro.send(42)
    # print(inspect.getgeneratorstate(my_coro))

    # my_coro = simple_coroutine()
    # my_coro.send(1729)

    my_coro2 = simple_coro2(14)
    from inspect import getgeneratorstate
    print(getgeneratorstate(my_coro2))
    print(next(my_coro2))
    print(getgeneratorstate(my_coro2))
    my_coro2.send(28)
    my_coro2.send(99)
    print(getgeneratorstate(my_coro2))


def test_average():
    coro_avg = averager()
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(5))
    try:
        coro_avg.send(None)
    except StopIteration as exc:
        result = exc.value
    print(result)


class DemoException(Exception):
    """An exception type for the demonstration"""

    def demo_exc_handling(self):
        print('-> coroutine started')
        try:
            while True:
                try:
                    x = yield
                except DemoException:
                    print('*** DemoException handled. Continuing')
                else:
                    print('-> coroutine received: {!r}'.format(x))
        finally:
            print('-> coroutine ending')


def test_coroutine_exception():
    de = DemoException()
    exc_coro = de.demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.send(22)
    # exc_coro.close()
    exc_coro.throw(ZeroDivisionError)
    print(getgeneratorstate(exc_coro))


def test_yield_from():
    def genYield():
        for c in 'AB':
            yield c
        for i in range(1, 3):
            yield i

    print(list(genYield()))

    def genYieldFrom():
        yield from 'AB'
        yield from range(1, 3)

    print(list(genYieldFrom()))


if __name__ == '__main__':
    test_yield_from()
