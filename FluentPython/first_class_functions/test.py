#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']


def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n - 1)


def test_factorial():
    print(factorial(42))
    print(factorial.__doc__)
    print(type(factorial))

    fact = factorial
    print(fact)
    print(fact(5))
    print(map(factorial, range(11)))
    print(list(map(fact, range(11))))


def reverse(word):
    return word[::-1]


def test_higher_order_functions():
    print(sorted(fruits, key=len))

    print(reversed('testing'))
    print(sorted(fruits, key=reverse))


def test_map():
    print(list(map(factorial, range(6))))
    print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
    print([factorial(n) for n in range(6) if n % 2])


def test_reduce():
    from functools import reduce
    from operator import add
    print(reduce(add, range(100)))


def test_lambda():
    print(sorted(fruits, key=lambda word: word[::-1]))


def test_callable_obj():
    print([callable(obj) for obj in (abs, str, 13)])


def test_user_defind_callbale():
    from first_class_functions.BingoCage import BingoCage
    bingo = BingoCage(range(3))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))


def test_introspection():
    class C: pass

    obj = C()

    def func(): pass

    print(sorted(set(dir(func)) - set(dir(obj))))


def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tag"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))

    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)

    else:
        return '<%s%s />' % (name, attr_str)


def test_functions_parameters():
    print(tag('br'))
    print(tag('p', 'hello'))
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', id=33))
    print(tag('p', 'hello', 'world', cls='sidebar'))
    print(tag(content='testing', name='img'))
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
    print(tag(**my_tag))


def clip(text: str, max_len: 'int > 0' = 80) -> str:
    """Return text clipped at the last space before or after max_len"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()


def test_clip():
    print(clip.__defaults__)
    print(clip.__code__)
    print(clip.__code__.co_argcount)

    from inspect import signature
    sig = signature(clip)
    print(sig)
    print(str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)

    print(clip.__annotations__)


def test_operator_module():
    from functools import reduce
    from operator import mul

    def fact(n):
        return reduce(lambda a, b: a * b, range(1, n + 1))

    def fact_op(n):
        return reduce(mul, range(1, n + 1))


def test_methodcaller():
    from operator import methodcaller
    s = 'The time has come'
    upcase = methodcaller('upper')
    print(upcase(s))
    hiphenate = methodcaller('replace', ' ', '-')
    print(hiphenate(s))


def test_partial():
    from operator import mul
    from functools import partial
    triple = partial(mul, 3)
    print(triple(7))
    print(list(map(triple, range(1, 10))))


if __name__ == '__main__':
    test_partial()
