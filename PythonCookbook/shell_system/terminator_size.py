#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os


def test_get_terminator_size():
    sz = os.get_terminal_size()
    print(sz)
    print(sz.columns)
    print(sz.lines)


if __name__ == '__main__':
    test_get_terminator_size()
