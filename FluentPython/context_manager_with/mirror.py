#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import contextlib


class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please Don\'t divide by zero!')
            return True


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    # yield 'JABBERWOCKY'
    sys.stdout.write = original_write
    msg = ''
    try:
        yield 'JABBERYWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


def test_lookingGlass():
    # with LookingGlass() as what:
    #     print('Alice, kitty and Snowdrop')
    #     print(what)
    #
    # manager = LookingGlass()
    # print(manager)
    # monster = manager.__enter__
    # print(monster)

    with looking_glass() as looking:
        print(looking)


if __name__ == '__main__':
    test_lookingGlass()
