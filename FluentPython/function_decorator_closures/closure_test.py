#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def test_arg():
    avg = Averager()
    print(avg(10))
    print(avg(10.5))
    print(avg(12))


def make_averager():
    series = []

    def averger(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averger


def test_make_averager():
    avg = make_averager()
    print(avg(10))
    print(avg(10.5))
    print(avg(12))


def make_averager_nonlocal():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


if __name__ == '__main__':
    test_make_averager()
