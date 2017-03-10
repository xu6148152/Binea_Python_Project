# coding=utf-8
import itertools

__author__ = 'xubinggui'

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
    print n
# print natuals

cs = itertools.cycle('ABC')
# for c in cs:
#     print c

ns = itertools.repeat('A', 10)
for c in ns:
    print c

for c in itertools.chain('ABC', 'XYZ'):
    print c

for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group)

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print key, list(group)

r = itertools.imap(lambda x: x*x, [1, 2, 3])
for c in r:
    print c

print '###############'
r = itertools.imap(lambda x: x*x, itertools.count(1))
for c in itertools.takewhile(lambda x: x < 100, r):
    print c

# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是迭代对象，只有用for循环迭代的时候才真正计算