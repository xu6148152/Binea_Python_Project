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

if __name__ == '__main__':
    test_lazyproperty()