#! python3
from collections import deque, defaultdict, OrderedDict
import heapq
import json

'''测试占位符* _'''
def test_placeholder():
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    # * _占位符
    *_, (year, month, day) = data
    print(name, shares, price, date)
    print(name, shares, price, year, month, day)

    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    name, email, *phone_numbers = record
    print(name, email, *phone_numbers)

'''利用deque保存最近一定数量的数据'''
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)


def get_n_largest(nums, n):
    return heapq.nlargest(n, nums)


def get_n_smallest(nums, n):
    return heapq.nsmallest(n, nums)


def test_search():
    with open(r'somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

'''测试hea'''
def test_heapq():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(get_n_largest(nums, 1))
    print(get_n_smallest(nums, 1))
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'APPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    ]
    print(heapq.nlargest(3, portfolio, key=lambda s: s['price']))

'''利用heapq构造优先队列'''
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


def test_priorityqueue():
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

def testDict():
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)

    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)

    print(d)

    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4

    for key in d:
        print(key, d[key])

    print(json.dumps(d))

if __name__ == '__main__':
    testDict()
