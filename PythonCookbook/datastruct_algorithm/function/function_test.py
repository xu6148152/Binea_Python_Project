#! python3
# -*- encoding: utf-8 -*-
from datastruct_algorithm.function.async import inlined_async, Async


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


def make_element(name, value, **attrs):
    import html
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=name, attrs=attr_str, value=html.escape(value))
    return element


def test_avg():
    print(avg(1, 2))
    print(avg(1, 2, 3, 4))


def test_make_element():
    print(make_element('item', 'Albatross', size='large', quantity=6))


def add(x: int, y: int) -> int:
    return x + y


def myfun():
    return 1, 2, 3


def test_add():
    print(help(add))
    print(add.__annotations__)


def test_myfun():
    print(myfun())


def test_lambda_add():
    add = lambda x, y: x + y
    print(add(2, 3))
    x = 10
    # 定义时绑定
    a = lambda y, x=x: x + y
    x = 20
    b = lambda y: x + y
    # 运行时绑定值
    print(a(10))
    print(b(10))

    funcs = [lambda x: x + n for n in range(5)]
    for f in funcs:
        print(f(0))

    funcs = [lambda x, n=n: x + n for n in range(5)]
    for f in funcs:
        print(f(0))


def spam(a, b, c, d):
    print(a, b, c, d)


def test_partial():
    from functools import partial
    s1 = partial(spam, 1)
    print(s1(2, 3, 4))
    s2 = partial(spam, d=42)
    print(s2(1, 2, 3))
    s3 = partial(spam, 1, 2, d=42)
    print(s3(3))


def apply_async(func, args, *, callback):
    result = func(*args)

    callback(result)


def print_result(result):
    print('Got:', result)


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler


def make_handler_coroutine():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


def test_apply_async():
    apply_async(add, (2, 3), callback=print_result)
    handler = make_handler()
    apply_async(add, (2, 3), callback=handler)
    handler = make_handler_coroutine()
    apply_async(add, (2, 3), callback=handler.send)


@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Done')


def sample():
    n = 0

    def func():
        print('n=', n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n
    func.set_n = set_n
    return func

def test_sample():
    f = sample()
    print(f())
    f.set_n(10)
    print(f())
    print(f.get_n())

def test_closure_instance():
    from datastruct_algorithm.function.closure_instance import Stack
    # s = Stack()
    # s.push(10)
    # s.push(20)
    # s.push('Hello')
    # # print(len(s))
    # print(s.pop())
    # print(s.pop())

    from timeit import timeit
    t = Stack()
    print(timeit('t.push(1); t.pop()', 'from __main__ import t'))
    from datastruct_algorithm.function.closure_instance import Stack2
    t = Stack2()
    print(timeit('t.push(1); t.pop()', 'from __main__ import t'))


if __name__ == '__main__':
    test_closure_instance()