# -*- encoding: utf-8 -*-
from queue import Queue
from threading import Thread


def producer(out_q, data):
    while True:
        out_q.put(data)


def consumer(in_q):
    while True:
        data = in_q.get()


def test_producer_consumer():
    q = Queue()
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q, []))
    t1.start()
    t2.start()


if __name__ == '__main__':
    test_producer_consumer()
