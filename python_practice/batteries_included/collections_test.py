# coding=utf-8
from collections import namedtuple, Counter
from collections import deque
from collections import defaultdict
import os
import sys

try:
    from collections import OrderedDict
except ImportError:
    # python 2.6 or earlier, use backport
    from ordereddict import OrderedDict

__author__ = 'xubinggui'

#namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p
print isinstance(p, tuple)

#deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q

#defaultdict
#key 不存在时，返回默认值
dd = defaultdict(lambda: 'N/A')
print dd['key']

#OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print d

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od

#FIFO dict
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)

#Counter
c = Counter()

for ch in 'programming':
    c[ch] = c[ch] + 1

print c
# print sys.version

#collections模块提供了一些有用的集合类

