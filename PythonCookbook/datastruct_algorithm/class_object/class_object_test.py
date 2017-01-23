#! python3
# -*- encoding: utf-8 -*-
def test_repr_str():
    from datastruct_algorithm.class_object.class_bundle import Pair
    p = Pair(3, 4)
    print(p)
    print('p is {0!r}'.format(p))
    print('p is {0}'.format(p))


def test_custom_date_format():
    from datastruct_algorithm.class_object.class_bundle import Date
    from datetime import date
    d = date.today()
    d = Date(d.year, d.month, d.day)
    print(format(d))
    print(format(d, 'mdy'))
    print('The date is {:ymd}'.format(d))


def test_lazy_connection():
    from functools import partial

    from datastruct_algorithm.class_object.class_bundle import LazyConnection
    conn = LazyConnection(('www.python.com', 80))

    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'HOST: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        print(resp)


def test_circle():
    from datastruct_algorithm.class_object.class_bundle import Circle
    c = Circle(4.0)
    print(c.radius)
    print(c.area)
    print(c.perimeter)


def test_extend():
    from datastruct_algorithm.class_object.class_bundle import B
    # print(B.__mro__)
    from datastruct_algorithm.class_object.class_bundle import SubPerson
    s = SubPerson('Guido')
    print(s)


def test_descriptor():
    from datastruct_algorithm.class_object.class_bundle import Stock
    s = Stock('a', 10, 15.0)
    print(s)


def test_lazyproperty():
    from datastruct_algorithm.class_object.class_bundle import Circle
    c = Circle(4.0)
    print(vars(c))
    print(c.area)
    print(vars(c))
    del c.area
    print(vars(c))
    print(c.area)


def test_sorteditems():
    from datastruct_algorithm.class_object.class_bundle import SortedItems
    items = SortedItems([5, 1, 3])
    print(list(items))
    items.add(2)
    print(list(items))


def test_proxy():
    class Spam:
        def __init__(self, x):
            self.x = x

        def bar(self, y):
            print('Spam.bar:', self.x, y)

    s = Spam(2)
    from datastruct_algorithm.class_object.class_bundle import Proxy
    p = Proxy(s)
    print(p.x)


def test_mixin():
    from datastruct_algorithm.class_object.class_bundle import LoggedMappingMixin
    class LoggedDict(LoggedMappingMixin, dict):
        pass

    d = LoggedDict()
    d['x'] = 23
    print(d['x'])
    del d['x']

    from collections import defaultdict

    from datastruct_algorithm.class_object.class_bundle import SetOnceMappingMixin
    class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
        pass

    d = SetOnceDefaultDict(list)
    d['x'].append(2)
    d['x'].append(3)
    print(d)


def test_state():
    from datastruct_algorithm.class_object.class_bundle import Connection1
    c = Connection1()
    print(c._state)
    c.open()
    print(c._state)
    print(c.read())
    print(c.write('hello'))
    c.close()
    print(c._state)


def test_getattr():
    from datastruct_algorithm.class_object.class_bundle import Point
    p = Point(2, 3)
    d = getattr(p, 'distance')(0, 0)
    print(d)

    import operator
    d = operator.methodcaller('distance', 0, 0)(p)
    print(d)

    points = [
        Point(1, 2),
        Point(3, 0),
        Point(10, -3),
        Point(-5, -7),
        Point(-1, 8),
        Point(3, 2)
    ]

    points.sort(key=operator.methodcaller('distance', 0, 0))
    print(points)


def test_visitor():
    from datastruct_algorithm.class_object.class_bundle import Number
    from datastruct_algorithm.class_object.class_bundle import Add
    from datastruct_algorithm.class_object.class_bundle import Evaluator
    a = Number(0)
    for n in range(1, 100000):
        a = Add(a, Number(n))

    e = Evaluator()
    print(e.visit(a))


def test_comparable():
    from datastruct_algorithm.class_object.class_bundle import House
    from datastruct_algorithm.class_object.class_bundle import Room
    h1 = House('h1', 'Cape')
    h1.add_room(Room('Master Bedroom', 14, 21))
    h1.add_room(Room('Living Room', 18, 20))
    h1.add_room(Room('Kitchen', 12, 16))
    h1.add_room(Room('Office', 12, 12))

    h2 = House('h2', 'Ranch')
    h2.add_room(Room('Master Bedroom', 14, 21))
    h2.add_room(Room('Living Room', 18, 20))
    h2.add_room(Room('Kitchen', 12, 16))

    h3 = House('h3', 'Split')
    h3.add_room(Room('Master Bedroom', 14, 21))
    h3.add_room(Room('Living Room', 18, 20))
    h3.add_room(Room('Office', 12, 16))
    h3.add_room(Room('Kitchen', 15, 17))

    houses = [h1, h2, h3]
    print('Is h1 bigger than h2?', h1 > h2)
    print('Is h2 smaller than h3?', h2 < h3)
    print('Which one is biggest?', max(houses))


def test_cache_object():
    import weakref

    class CachedSpamManager:
        def __init__(self):
            self._cache = weakref.WeakValueDictionary()

        @staticmethod
        def get_spam(self, name):
            if name not in self._cache:
                s = Spam._new(name)
                self._cache[name] = s
            else:
                s = self._cache[name]

            return s

        def clear(self):
            self._cache.clear()

    class Spam:
        # _spam_cache = weakref.WeakValueDictionary()
        manager = CachedSpamManager()

        # def __new__(cls, name):
        #     if name in cls._spam_cache:
        #         return cls._spam_cache[name]
        #
        #     else:
        #         self = super().__new__(cls)
        #         cls._spam_cache[name] = self

        # def __init__(self, name):
        #     print('Initializing Spam')
        #     self.name = name

        # def get_spam(self, name):
        #     return Spam.manager.get_spam(name)

        @classmethod
        def _new(cls, name):
            self = cls.__new__(cls)
            self.name = name
            return self
    c = CachedSpamManager()
    s = c.get_spam('Dave')
    print(s)
    t = c.get_spam('Dave')
    print(t)
    print(s is t)


if __name__ == '__main__':
    test_cache_object()
