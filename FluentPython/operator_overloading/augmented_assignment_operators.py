#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from interfaces_protocols.bingocage import BingoCage
from interfaces_protocols.tombola import Tombola
from sequence_hacking_hashing_slicing.vector import Vector

v1 = Vector([1, 2, 3])

v1_alias = v1
id(v1)
v1 += Vector([4, 5, 6])
print(v1)


class AddableBingoCage(BingoCage):
    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = "right operand in += must be {!r} or an iterable"
                raise TypeError(msg.format(self_cls))

        self.load(other_iterable)
        return self
