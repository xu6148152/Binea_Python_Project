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


def test_dict_compute():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    # zip的结果只能访问一次
    min_price = min(zip(prices.values(), prices.keys()))
    print(min_price)
    max_price = max(zip(prices.values(), prices.keys()))
    print(max_price)

    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    print(prices_sorted)

    print(min(prices, key=lambda k: prices[k]))
    print(max(prices, key=lambda k: prices[k]))


def test_dict_same():
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2,
    }

    print(a.keys() & b.keys())
    print(a.keys() - b.keys())
    print(a.items() & b.items())


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def test_dedupe():
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))

def test_slice():
    items = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 4)
    print(items[a])
    items[a] = [10, 11]
    print(items)
    del items[a]
    print(items)


def test_counter():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    ]

    from collections import Counter
    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print(top_three)


def test_itemgetter():
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]

    from operator import itemgetter

    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    print(rows_by_fname)
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    print(rows_by_uid)


def test_groupby():
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'}
    ]

    from operator import itemgetter
    from itertools import groupby

    rows.sort(key=itemgetter('date'))
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(' ', i)

def test_filter():
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    # generator
    pos = (n for n in mylist if n > 0)
    for x in pos:
        print(x)

    ivals = list(filter(is_int, mylist))
    print(ivals)


def is_int(val):
    try:
        x = int(val)
        return x > 0
    except ValueError:
        return False


def test_compress():
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'}
    ]

    counts = [0, 3, 10, 4, 1, 7, 6, 1]

    from itertools import compress
    more5 = [n > 5 for n in counts]
    print(more5)
    print(list(compress(rows, more5)))


def test_subdict():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    p1 = {key: value for key, value in prices.items() if value > 200}
    print(p1)


def test_namedtuple():
    from collections import namedtuple
    Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    sub = Subscriber('jonesy@example.com', '2012-10-19')
    print(sub)
    print(sub.addr)
    print(sub.joined)


def dict_to_stock(s):
    from collections import namedtuple
    Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
    stock_prototype = Stock('', 0, 0.0, None, None)
    stock_prototype._replace(**s)


def test_dict_to_namedtuple():
    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    print(dict_to_stock(a))


def test_chain_map():
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}

    from collections import ChainMap
    c = ChainMap(a, b)
    print(c['z'])


if __name__ == '__main__':
    test_chain_map()

