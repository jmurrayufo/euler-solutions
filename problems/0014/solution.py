#!/usr/bin/env python3

import math
import time
import numpy as np

t0 = time.time()

def colaz_len(num):
    count = 1
    while num != 1:
        count += 1
        if num % 2:
            num = num*3+1
        else:
            num /= 2
    return count

longest = 0

for i in range(1,1000000):
    l = colaz_len(i)
    if l > longest:
        longest = l
        print(i,l)

print(time.time()-t0)
