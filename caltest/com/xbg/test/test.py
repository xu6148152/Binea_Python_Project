import math
import os

__author__ = 'xubinggui'

def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)

    return nx, ny

print(move(100, 100, 2))

def calc(*abc):
    sum = 0
    for n in abc:
        sum = sum + n * n
    return sum

print(calc())

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

print(person('Michael', 30, city ='beijing'))

L = ['Michael', 'Sarah', 'Tracy']
print(L[:])

d = {'a': 1, 'b': 2, 'c': 3}

for i, value in d.items():
    print(i, value),

print()

for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

print(range(1, 11))

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])

print([d for d in os.listdir('.')])

g = (x * x for x in range(1, 11) if x % 2 == 0)
print(g.next())

def f(x):
    return x * x

print(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))