#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import sys
import time


def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))


def modified_within(top, seconds):
    now = time.time()
    for path, dirs, files in os.walk(top):
        for name in files:
            fullpath = os.path.join(path, name)
            if os.path.exists(fullpath):
                mtime = os.path.getmtime(fullpath)
                if mtime > (now - seconds):
                    print(fullpath)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('lack arguments')
        raise SystemExit(1)
    # findfile(sys.argv[1], sys.argv[2])
    modified_within(sys.argv[1], float(sys.argv[2]))