#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))

if __name__ == '__main__':
    x = Gizmo()