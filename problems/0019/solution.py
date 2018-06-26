#!/usr/bin/env python3

from itertools import permutations
import datetime
import math
import numpy as np
import time

t0 = time.time()

d = datetime.date(1901, 1, 1)
first_sundays = 0
while d <= datetime.date(2000,12,31):
    if d.day == 1 and d.weekday() == 6:
        first_sundays += 1
    d += datetime.timedelta(days=1)
print(first_sundays)
print(time.time()-t0)
