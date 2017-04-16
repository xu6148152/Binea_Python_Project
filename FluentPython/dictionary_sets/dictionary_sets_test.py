#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import collections


def test_hash():
    tt = (1, 2, (30, 40))
    print(hash(tt))
    tl = (1, 2, [30, 40])
    print(hash(tl))


def test_dict_comp():
    DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

    country_code = {country: code for code, country in DIAL_CODES}
    # print(country_code)
    print({code: country.upper() for country, code in country_code.items() if code < 66})


def test_none_key():
    import sys
    import re

    WORD_RE = re.compile('\w+')

    index = {}
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                occurrences = index.get(word, [])
                occurrences.append(location)
                index[word] = occurrences
    for word in sorted(index, key=str.upper):
        print(word, index[word])


def test_counter():
    ct = collections.Counter('dsakfjdjsfakdjfs')
    print(ct)


def test_mappingproxy():
    from types import MappingProxyType
    d = {1: 'A'}
    d_proxy = MappingProxyType(d)
    print(d_proxy)
    d_proxy[2] = 'x'


def test_set():
    l = ['spam', 'spam', 'eggs', 'spam']
    print(set(l))


def test_set_literals():
    from dis import dis
    print(dis('set([1])'))


def test_set_comprehension():
    from unicodedata import name
    print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})


if __name__ == '__main__':
    test_set_comprehension()
