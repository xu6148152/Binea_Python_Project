#! python3
# -*- encoding: utf-8 -*-

from queue import Queue
from functools import wraps


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper


class Async:
    def __int__(self, func, args):
        self.func = func
        self.args = args
