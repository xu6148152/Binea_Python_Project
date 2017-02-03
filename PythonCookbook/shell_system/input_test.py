#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')
# def test_fileinput():



# if __name__ == '__main__':
#     test_fileinput()
