#! /usr/bin/python

import time

start = time.time()
print("time")
seconds = 0.000
left = 0.0
delta = 0.001
while left < 5:
    print(left, seconds)
    while (left -seconds) < delta:
        end = time.time()
        left = end - start
    seconds = left
print("stop")
