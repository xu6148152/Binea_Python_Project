#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from pythonic_object.vector2d import Vector2d

v1 = Vector2d(3, 4)
print(v1.x, v1.y)
v1_clone = eval(repr(v1))
print(v1 == v1_clone)

print(bytes(v1))

print(hash(v1))