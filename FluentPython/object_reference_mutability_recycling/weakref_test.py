#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())

a_set = {2, 3, 4}
print(wref())
print(wref() is None)
print(wref() is None)


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


import weakref

stock = weakref.WeakKeyDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))

del catalog
print(stock.keys())
del cheese
print(sorted(stock.keys()))
