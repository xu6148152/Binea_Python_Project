#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import dis
import bisect
import sys
from array import array
from random import random

symbols = '$¢£¥€¤'


def test1():
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    print(codes)


def test2():
    codes = [ord(symbol) for symbol in symbols]
    print(codes)


def test3():
    x = 'my precious'
    dummy = [x for x in 'ABC']
    print(x)


def test4():
    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    print(beyond_ascii)

    beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
    print(beyond_ascii)


TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""


def test_speed():
    import speed_test

    speed_test.clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]', SETUP, TIMES)
    speed_test.clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]', SETUP, TIMES)
    speed_test.clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))', SETUP, TIMES)
    speed_test.clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))', SETUP, TIMES)


def test_cartesian():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    print(tshirts)

    for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(tshirt)


def test_generator_exp():
    tp = tuple(ord(symbol) for symbol in symbols)
    print(tp)
    import array
    ar = array.array('I', (ord(symbol) for symbol in symbols))
    print(ar)


def test_tuple_records():
    lax_coordinates = (33.9425, -118.408056)
    city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
    for passport in sorted(traveler_ids):
        print('%s/%s' % passport)

    for country, _ in traveler_ids:
        print(country)


def test_tuple_unpack():
    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates
    print('{0}, {1}'.format(latitude, longitude))
    print('%s, %s' % (latitude, longitude))

    a, b, *rest = range(5)
    print(a, b, rest)


def test_named_tuple():
    from collections import namedtuple
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print(tokyo)

    print(tokyo._fields)

    LatLong = namedtuple('LatLong', 'lat long')
    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
    delhi = City._make(delhi_data)
    print(delhi._asdict())


def test_slice_objects():
    s = 'bicycle'
    print(s[::3])
    print(s[::-1])
    print(s[::-2])

    l = [1, 2, 3]
    print(l * 3)

    t = (1, 2, [30, 40])
    t[2] += [50, 60]
    print(t)


def test_bisect():
    HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
    NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

    ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

    def demo(bisect_fn):
        for needle in reversed(NEEDLES):
            position = bisect_fn(HAYSTACK, needle)
            offset = position * '  |'
            print(ROW_FMT.format(needle, position, offset))

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect_right

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)


def test_bisect_1():
    def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
        i = bisect.bisect(breakpoints, score)
        return grades[i]

    print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])


def test_bisect_insort():
    import random

    SIZE = 7
    random.seed(1729)

    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE * 2)
        bisect.insort(my_list, new_item)
        print('%sd ->' % new_item, my_list)


def test_array():
    floats = array('d', (random() for i in range(10 ** 7)))
    print(floats[-1])


def test_memory_view():
    numbers = array('h', [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)
    print(len(memv))
    print(memv[0])
    memv_oct = memv.cast('B')
    print(memv_oct.tolist())
    memv_oct[5] = 4
    print(numbers)


def test_deque():
    from collections import deque
    dq = deque(range(10), maxlen=10)
    print(dq)
    dq.rotate(3)
    print(dq)
    dq.rotate(-4)
    print(dq)
    dq.appendleft(-1)
    print(dq)

if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    # test_speed()
    # test_cartesian()
    # test_generator_exp()
    # test_tuple_records()
    # test_tuple_unpack()
    # test_named_tuple()
    # test_slice_objects()
    # dis.dis('s[a] += b')
    # test_bisect_1()
    # test_bisect_insort()
    # test_array()
    # test_memory_view()
    test_deque()
