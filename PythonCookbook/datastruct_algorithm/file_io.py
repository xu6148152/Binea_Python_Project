#! python3
# -*- encoding: utf-8 -*-

# f = open('hello.txt', 'rt', newline='')
# print(f.read())

with open('hello.txt', 'wt') as f:
    print('Hello World', file=f)

