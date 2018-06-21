#!/usr/bin/env python3

nums = set()

for i in range(3,1000):
    if i % 3 == 0 or i % 5 == 0:
        nums.add(i)
print(sum(nums))
