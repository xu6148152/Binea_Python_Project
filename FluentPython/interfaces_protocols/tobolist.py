#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from random import randrange
from interfaces_protocols.tombola import Tombola


@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


print(issubclass(TomboList, Tombola))
t = TomboList(range(100))
print(isinstance(t, Tombola))

print(TomboList.__mro__)
