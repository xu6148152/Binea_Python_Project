#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Demo:
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


print(Demo.klassmeth())

print(Demo.klassmeth('spam'))

print(Demo.statmeth())

print(Demo.statmeth('spam'))
