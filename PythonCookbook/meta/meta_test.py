# -*- encoding: utf-8 -*-
import inspect
import time
from functools import wraps, partial
from inspect import signature


def timethis(func):
    '''
    Decorator that reports the execution time
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


def test_timethis():
    @timethis
    def countdown(n):
        '''
        count down
        '''
        while n > 0:
            n -= 1

    print(countdown(10000))
    print(countdown.__name__)
    print(countdown.__doc__)
    print(countdown.__annotations__)
    print(countdown.__wrapped__(100000))


def test_unwrapper():
    @timethis
    def add(x, y):
        return x + y

    origin_add = add.__wrapped__
    print(origin_add(3, 4))
    print(add(3, 4))


import logging


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    '''
    Add logging to a function. level is the logging
    level, name is the logger name, and message is
    the log message. If name and message aren't specified.
    they default to the function's module and name.
    '''

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kargs):
            log.log(level, logmsg)
            return func(*args, **kargs)

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper

    return decorate


def logged_variable_params(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


def test_logged():
    @logged(logging.DEBUG)
    def add(x, y):
        return x + y

    @logged(logging.CRITICAL, 'example')
    def spam():
        print('Spam!')

    # add(2, 3)
    # spam()

    logging.basicConfig(level=logging.DEBUG)
    add(2, 3)
    add.set_message('Add called')
    add(2, 3)
    add.set_level(logging.WARNING)
    add(2, 3)


def test_logged_variable_params():
    # Example use
    @logged_variable_params
    def add(x, y):
        return x + y

    # @logged_variable_params(level=logging.CRITICAL, name='example')
    # def spam():
    #     print('Spam!')

    add(2, 3)
    # spam()


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func

        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))
            return func(*args, **kwargs)

        return wrapper

    return decorate


def test_typeassert():
    @typeassert(int, z=int)
    def spam(x, y, z=42):
        print(x, y, z)

    print(spam(1, 2, 3))


def test_profiled():
    from meta.profiled import Profiled
    @Profiled
    def add(x, y):
        return x + y

    class Spam:
        @Profiled
        def bar(self, x):
            print(self, x)

    print(add(2, 3))
    add(4, 5)
    print(add.ncalls)
    s = Spam()
    print(s.bar(1))
    s.bar(2)
    s.bar(3)
    print(Spam.bar.ncalls)


def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug', inspect.Parameter.KEYWORD_ONLY, default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper


def test_optional_debug():
    @optional_debug
    def spam(a, b, c):
        print(a, b, c)

    print(spam(1, 2, 3, debug=True))


def log_getattribute(cls):
    # GEt the original implementation
    orig_getattribute = cls.__getattribute__

    # Make a new definition
    def new_getattribute(self, name):
        print('getting:', name)
        return orig_getattribute(self, name)

    # Attach to the class and return
    cls.__getattribute__ = new_getattribute
    return cls


def test_log_getattribute():
    @log_getattribute
    class A:
        def __init__(self, x):
            self.x = x

        def Spam(self):
            pass

    a = A(42)
    print(a.x)


def test_singleton():
    from meta.singleton import Singleton
    class Spam(metaclass=Singleton):
        def __init__(self):
            print('Creating Spam')

    a = Spam()
    b = Spam()
    print(a is b)
    c = Spam()
    print(a is c)


def test_capture_class_attribute():
    from meta.typed import Stock
    s = Stock('GOOG', 100, 490.1)
    print(s.name)
    print(s.as_csv())
    # t = Stock('AAPl', 'a lot', 610.23)


def test_metaclass_optional_arguments():
    from meta.my_meta import MyMeta

    class Spam(metaclass=MyMeta):
        debug = True
        synchronize = True
        pass

    s = Spam()
    print(s)


def test_inspect():
    from inspect import Signature, Parameter
    parms = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
             Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
             Parameter('z', Parameter.KEYWORD_ONLY, default=None)]
    sig = Signature(parms)
    print(sig)

    def func(*args, **kwargs):
        bound_values = sig.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            print(name, value)

    print(func(1, 2, z=3))

    def make_sig(*names):
        parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
        return Signature(parms)

    class Structure:
        __signature__ = make_sig()

        def __init__(self, *args, **kwargs):
            bound_values = self.__signature__.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                setattr(self, name, value)

    class Stock(Structure):
        __signature__ = make_sig('name', 'shares', 'price')

    class Point(Structure):
        __signature__ = make_sig('x', 'y')

    print(inspect.signature(Stock))


def test_define_classes_program():
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    cls_dict = {
        '__init__': __init__,
        'cost': cost,
    }

    import types
    import abc
    Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
    Stock.__module__ = __name__
    s = Stock('ACME', 50, 91.1)
    print(s.cost())

    Stock = types.new_class('Stock', (), {'metaclass': abc.ABCMeta}, lambda ns: ns.update(cls_dict))
    Stock.__module__ = __name__
    print(type(Stock))


def named_tuple(classname, fieldnames):
    import operator
    import types
    import sys

    cls_dict = {name: property(operator.itemgetter(n)) for n, name in enumerate(fieldnames)}

    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__

    cls = types.new_class(classname, (tuple,), {}, lambda ns: ns.update(cls_dict))

    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls


def test_named_tuple():
    Point = named_tuple('Point', ['x', 'y'])
    print(Point)


def test_function_annotation():
    from meta.multiple import MultipleMeta
    class Spam(metaclass=MultipleMeta):
        def bar(self, x: int, y: int):
            print('Bar 1:', x, y)

        def bar(self, s: str, n: int = 0):
            print('Bar 2:', s, n)

    import time

    class Date(metaclass=MultipleMeta):
        def __init__(self, year: int, month: int, day: int):
            self.year = year
            self.month = month
            self.day = day

        def __init__(self):
            t = time.localtime()
            self.__init__(t.tm_year, t.tm_mon, t.tm_mday)

    s = Spam()
    print(s.bar(2, 3))
    print(s.bar('hello'))
    print(s.bar('hello', 5))
    # print(s.bar(2, 'hello'))
    d = Date(2012, 12, 21)
    e = Date()
    print(e.year)
    print(e.month)
    print(e.day)


def test_contextmanager():
    import time
    from contextlib import contextmanager

    @contextmanager
    def timethis(label):
        start = time.time()
        try:
            yield
        finally:
            end = time.time()
            print('{}: {}'.format(label, end - start))

    with timethis('counting'):
        n = 1000000
        while n > 0:
            n -= 1

    @contextmanager
    def list_transaction(orig_list):
        working = list(orig_list)
        yield working
        orig_list[:] = working

    items = [1, 2, 3]
    with list_transaction(items) as working:
        working.append(4)
        working.append(5)
        raise RuntimeError('oops')

    print(items)


def test_local_exec():
    a = 13
    # loc = locals()
    loc = {'a': a}
    glb = {}
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print(b)


def test_ast():
    import ast
    ex = ast.parse('2 + 3 * 4 + x', mode='eval')
    print(ex)
    print(ast.dump(ex))


def test_code_analyzer():
    import ast
    code = \
        '''
        for i in range(10):
            print(i)
        del i
        '''

    top = ast.parse(code, mode='exec')

    from meta.code_analyzer import CodeAnalyzer
    c = CodeAnalyzer()
    c.visit(top)
    print('Loaded:', c.loaded)
    print('Stored:', c.stored)
    print('Deleted:', c.deleted)

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('Blastoff!')


def test_python_bytecode():
    # import dis
    # print(dis.dis(countdown))
    c = countdown.__code__.co_code
    print(c)

    import opcode
    print(opcode.opname[c[0]])


def generate_opcodes(codebytes):
    import opcode
    extended_arg = 0
    i = 0
    n = len(codebytes)
    while i < n:
        op = codebytes[i]
        i += 1
        if op >= opcode.HAVE_ARGUMENT:
            oparg = codebytes[i] + codebytes[i + 1] * 256 + extended_arg
            extended_arg = 0
            i += 2
            if op == opcode.EXTENDED_ARG:
                extended_arg = oparg * 65536
                continue
        else:
            oparg = None

        yield (op, oparg)


def test_generate_opcodes():
    import opcode
    for op, oparg in generate_opcodes(countdown.__code__.co_code):
        print(op, opcode.opname[op], oparg)


if __name__ == '__main__':
    test_generate_opcodes()