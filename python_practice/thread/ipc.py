# coding=utf-8
# -*- coding: UTF-8 -*-

from multiprocessing.queues import Queue
from multiprocessing import Process
import random
import time

__author__ = 'xubinggui'

# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


# 在Unix/Linux下，可以使用fork()调用实现多进程。
#
# 要实现跨平台的多进程，可以使用multiprocessing模块。
#
# 进程间通信是通过Queue、Pipes等实现的。