#!/usr/bin/env python3

import math
import time
import numpy as np

t0 = time.time()

class trip:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def valid(self):
        if self.x < self.y and self.y < self.z and self.x**2+self.y**2==self.z**2:
            return True
        return False


for a in range(1001):
    for b in range(a,1001):
        for c in range(b,1001):
            if a+b+c != 1000:
                continue
            sol = trip(a,b,c)
            if sol.valid():
                print(a,b,c)
                print(a*b*c)
                



print(time.time()-t0)
