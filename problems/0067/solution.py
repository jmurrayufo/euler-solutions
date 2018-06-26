#!/usr/bin/env python3

import math
import time
import numpy as np
from itertools import permutations

t0 = time.time()

tri = ""
with open("triangle.txt","r") as fp:
    for line in fp:
        tri += line

rows = []
for row in tri.split("\n"):
    row=row.lstrip().rstrip()
    if row == "":
        continue
    rows.append([int(x) for x in row.split(" ")])

for i in range(-2, -len(rows)-1, -1):
    print()
    print(rows[i])
    for col in range(len(rows[i])):
        rows[i][col] += max(rows[i+1][col], rows[i+1][col+1])
        print(col, rows[i][col])
    print(rows[i])
    time.sleep(1)

print(time.time()-t0)
