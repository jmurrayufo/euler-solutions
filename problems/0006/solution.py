#!/usr/bin/env python3

import math
import time

t0 = time.time()

sum_squares = 0
squared_sum = 0

for i in range(101):
    sum_squares += i*i
    squared_sum += i

squared_sum *= squared_sum

print(squared_sum, sum_squares, squared_sum - sum_squares)

print(time.time()-t0)
