#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time

# Display the program's instructions.
print("Press enter to begin. Afterwards, press enter to lapNum = 1'click' the stopwatch. Press Ctrl-C to quit")

input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1
# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone')
