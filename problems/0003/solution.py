#!/usr/bin/env python3

import math
import time

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def prime_list():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1

remainder = 600851475143
factors = []

for i in prime_list():

    if i >= remainder:
        break

    while remainder % i == 0:
        factors.append(i)
        remainder /= i
        remainder = int(remainder)


print(remainder, factors)

