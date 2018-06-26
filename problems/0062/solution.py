#!/usr/bin/env python3

import math
import time
import numpy as np
from itertools import permutations
from collections import defaultdict

t0 = time.time()

vals = defaultdict(lambda: 0)


base = 0
while True:
    cube = base**3
    cube = str(cube)
    cube = sorted(cube)
    cube = "".join(cube)

    if cube == "012334556789":
        print(base)
        break

    vals[cube] += 1

    if vals[cube] == 5:
        break

    base += 1

print(vals[cube], cube, base)

print(time.time()-t0)
