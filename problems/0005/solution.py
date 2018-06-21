#!/usr/bin/env python3

import math
import time

t0 = time.time()

i = 0
smolest_n = 21

while True:
    i += 1
    for n in range(20, 1, -1):
        if i%n:
            break
        if n < smolest_n:
            smolest_n = n
            print(i, n)
    else:
        break

print(i)

print(time.time()-t0)
