#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

def deco(func):
    def inner():
        print('running inner()')

    return inner


@deco
def target():
    print('running target()')


def test_deco():
    target()


if __name__ == '__main__':
    test_deco()

