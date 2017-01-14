#! python3
# -*- encoding: utf-8 -*-
from dateutil.rrule import *


def test_round():
    # 返回离它最近的偶数
    print(round(1.5))
    print(round(2.5))
    print(format(1.23456, '0.2f'))


def test_decimal():
    from decimal import localcontext
    from decimal import Decimal
    a = Decimal('1.3')
    b = Decimal('1.7')
    print(a / b)

    with localcontext() as ctx:
        ctx.prec = 3
        print(a / b)
    # 次方
    print(3 ** 3)


def test_byte_pack_unpack():
    data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    print(len(data))
    print(int.from_bytes(data, 'little'))
    print(int.from_bytes(data, 'big'))

    x = 94522842520747284487117727783387188
    print(x.to_bytes(16, 'big'))
    print(x.to_bytes(16, 'little'))

    import struct
    hi, lo = struct.unpack('>QQ', data)
    print(((hi << 64) + lo))


def test_complex():
    a = complex(2, 4)
    b = 3 - 5j
    print(a, b)

    import numpy as np
    a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
    print(a)

    import cmath
    print(cmath.sqrt(-1))


def test_nan():
    a = float('inf')
    print(a)
    import math
    print(math.isinf(a))


def test_fractions():
    from fractions import Fraction
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    print(a + b)


def test_numpy_array():
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]
    print(x * 2)
    print(x + y)

    import numpy as np
    ax = np.array([1, 2, 3, 4])
    ay = np.array([5, 6, 7, 8])
    print(ax * 2)

def test_numpy_matrix():
    import numpy as np
    m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
    print(m)
    # transpose(翻转)
    print(m.T)
    # inverse(反转)
    print(m.I)

    # Determinant
    print(np.linalg.det(m))

def test_random():
    import random
    values = [1, 2, 3, 4, 5, 6]
    print(random.choice(values))

    print(random.sample(values, 2))
    random.shuffle(values)
    print(values)
    print(random.randint(0, 10))
    print(random.random())
    print(random.getrandbits(1000))

def test_datetime():
    from datetime import timedelta
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print(c.days)

    from datetime import datetime
    a = datetime(2017, 1, 14)
    print(a + timedelta(days=10))
    print(datetime.today())

    from dateutil.relativedelta import relativedelta
    d = datetime.now()
    # next Friday
    print(d + relativedelta(weekday=FR))
    # previous Friday
    print(d + relativedelta(weekday=FR(-1)))

def test_calendar():
    from datetime import timedelta
    a_day = timedelta(days=1)
    first_day, last_day = get_month_range()
    while first_day < last_day:
        print(first_day)
        first_day += a_day

def get_month_range(start_date=None):
    from datetime import date, timedelta
    import calendar
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)

def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step

def test_date_range():
    from datetime import date, datetime, timedelta
    for d in date_range(datetime(2017, 1, 14), datetime(2017, 1, 24), timedelta(hours=6)):
        print(d)

def test_string_to_date():
    from datetime import datetime
    text = '2017-01-16'
    y = datetime.strptime(text, '%Y-%m-%d')
    z = datetime.now()
    diff = z - y
    print(diff)

def parse_ymd(s):
    from datetime import datetime
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))

def test_timezone():
    from datetime import datetime
    from pytz import timezone
    d = datetime.now()
    central = timezone('US/Central')
    loc_d = central.localize(d)
    print(loc_d)


if __name__ == '__main__':
    test_timezone()