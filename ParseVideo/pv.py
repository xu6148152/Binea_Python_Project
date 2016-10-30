# -*-coding:utf8-*-
import os,sys


def start():
    sys.path.insert(0, os.path.dirname(__file__))
    from bin import parse_video
    parse_video.main(sys.argv[1:])

if __name__ == '__main__':
    start()