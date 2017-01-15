#! python3
# -*- encoding: utf-8 -*-

def test_iter():
    items = [1, 2, 3]
    it = iter(items)
    # for i in items:
    #     print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    # StopIteration
    print(next(it))


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


class DepthFirstIterator(object):
    '''
    Depth-first traversal
    '''

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        # If processing a child, return its next item
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        # Advance to the next child and start its iteration
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)


def test_node_iteration():
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


def test_frange():
    for n in frange(0, 4, 0.5):
        print(n)


class Countdown:
    def __init__(self, start):
        self._start = start

    # Forward iterator
    def __iter__(self):
        n = self._start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self._start:
            yield n
            n += 1


def test_countdown():
    for rr in reversed(Countdown(30)):
        print(rr, end='')
        print(',', end='')
    print()
    for rr in Countdown(30):
        print(rr, end='')
        print(',', end='')


def count(n):
    while True:
        yield n
        n += 1


def test_slice_iterator():
    c = count(0)
    import itertools
    for x in itertools.islice(c, 10, 20):
        print(x)


def test_dropwhile():
    from itertools import dropwhile
    import codecs
    with codecs.open('./descend_parser.py', 'r', 'utf-8') as f:
        for line in dropwhile(lambda line: line.startswith('#'), f):
            print(line, end='')
            # while True:
            #     line = next(f, '')
            #     if not line.startswith('#'):
            #         break
            # while line:
            #     print(line, end='')
            #     line = next(f, None)


def test_permutations():
    items = ['a', 'b', 'c']
    from itertools import permutations
    for p in permutations(items):
        print(p)


def test_combinations():
    items = ['a', 'b', 'c']
    from itertools import combinations
    for c in combinations(items, 3):
        print(c)
    from itertools import combinations_with_replacement
    for c in combinations_with_replacement(items, 3):
        print(c)

def test_enumerate():
    my_list = ['a', 'b', 'c']
    for idx, val in enumerate(my_list):
        print(idx, val)

def test_zip():
    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 37, 15, 62, 99, 120]
    for x, y in zip(xpts, ypts):
        print(x, y)
    from itertools import zip_longest
    for i in zip_longest(xpts, ypts):
        print(i)

def test_chain():
    from itertools import chain
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']
    for x in chain(a, b):
        print(x)

def flatten(items, ignore_type=(str, bytes)):
    from collections import Iterable
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_type):
            yield from flatten(x)
        else:
            yield x

def test_flatten():
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    for x in flatten(items):
        print(x)

    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    for x in flatten(items):
        print(x)

def test_heap_merge():
    import heapq
    a = [1, 4, 7, 10]
    b = [2, 5, 6, 11]
    for c in heapq.merge(a, b):
        print(c)

def test_iter_replace_while():
    import sys
    f = open('./dropwhile_test.py')
    for chunk in iter(lambda: f.read(10), ''):
        sys.stdout.write(chunk)

if __name__ == '__main__':
    test_iter_replace_while()