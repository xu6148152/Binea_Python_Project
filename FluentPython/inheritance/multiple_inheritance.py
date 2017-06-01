#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


d = D()


# print(d.pong())
# print(C.pong(d))
#
# print(D.__mro__)

# d.pingpong()
# d.pingpong()

def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))


# print(bool.__mro__)
#
import tkinter

#
# print_mro(tkinter.Text)


print_mro(tkinter.Toplevel)
print_mro(tkinter.Widget)
print_mro(tkinter.Button)
print_mro(tkinter.Entry)
print_mro(tkinter.Text)
