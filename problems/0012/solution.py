#!/usr/bin/env python3

import math
import time
import numpy as np

t0 = time.time()

def tri_gen(start=1):
    top = int(start)
    while True:
        top += 1
        yield sum([x for x in range(top)])

def divisors(num):
    divs = []

    for i in range(1,int(num/2+1)):
        if num % i == 0:
            divs.append(i)

    return divs


biggest_divs = 0

for num in tri_gen(start=1):
    divs = divisors(num)

    if len(divs) > 500:
        break

    if len(divs) > biggest_divs:
        biggest_divs = len(divs)
        print(num,len(divs))
print(divs)
print(num)

print(time.time()-t0)
