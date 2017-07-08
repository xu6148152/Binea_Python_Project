#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return


def test_gen_123():
    def gen_123():
        yield 1
        yield 2
        yield 3

    # for i in gen_123():
    #     print(i)

    g = gen_123()
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))


if __name__ == '__main__':
    test_gen_123()
