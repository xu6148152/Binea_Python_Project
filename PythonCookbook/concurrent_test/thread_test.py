# -*- encoding: utf-8 -*-
from threading import Thread, Event

import time


def countdown(n):
    import time
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


def test_thread():
    # t = Thread(target=countdown, args=(10,), daemon=True)
    # t.start()

    started_evt = Event()
    print('Launching countdown')
    t = Thread(target=countdown, args=(10, started_evt))
    t.start()

    started_evt.wait()
    print('countdown is running')


def test_countdown_task():
    from concurrent.task import CountdownTask
    c = CountdownTask()
    t = Thread(target=c.run, args=(10,))
    t.start()
    c.terminate()
    t.join()


def test_periodic_timer():
    from concurrent.periodic_timer import PeriodicTimer
    ptimer = PeriodicTimer(5)
    ptimer.start()

    def countdown1(nticks):
        while nticks > 0:
            ptimer.wait_for_tick()
            print('T-minus', nticks)
            nticks -= 1

    def countup(last):
        n = 0
        while n < last:
            ptimer.wait_for_tick()
            print('Counting', n)
            n += 1

    Thread(target=countdown1, args=(10,)).start()
    Thread(target=countup, args=(5,)).start()


if __name__ == '__main__':
    test_periodic_timer()
