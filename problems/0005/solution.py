#!/usr/bin/env python3

import math
import time

from itertools import permutations

t0 = time.time()

digits = [0,1,2,3,4,5,6,7,8,9]

valid_nums = []

for i in permutations(digits):
    num = f"{i[0]}{i[1]}{i[2]}{i[3]}{i[4]}{i[5]}{i[6]}{i[7]}{i[8]}{i[9]}"
    # for n in i:
    #     num += str(n)

    if int(f"{num[7]}{num[8]}{num[9]}") % 17:
        continue
    if int(f"{num[6]}{num[7]}{num[8]}") % 13:
        continue
    if int(f"{num[5]}{num[6]}{num[7]}") % 11:
        continue
    if int(f"{num[4]}{num[5]}{num[6]}") % 7:
        continue
    if int(f"{num[3]}{num[4]}{num[5]}") % 5:
        continue
    if int(f"{num[2]}{num[3]}{num[4]}") % 3:
        continue
    if int(f"{num[1]}{num[2]}{num[3]}") % 2:
        continue
    print(num)
    valid_nums.append(int(num))

print(sum(valid_nums))

print(time.time()-t0)
