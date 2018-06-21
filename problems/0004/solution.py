#!/usr/bin/env python3

import math
import time


def is_pal(num):
    assert type(num) == int 

    num = str(num)
    for i in range(1,math.ceil(len(num)/2)+1):
        if num[i-1] != num[-i]:
            return False
    return True

big = 0
t0 = time.time()

for x in range(100,1000):
    for y in range(100,1000):
        if x*y > big and is_pal(x*y):
            big = y*x

print(big)

print(time.time()-t0)
