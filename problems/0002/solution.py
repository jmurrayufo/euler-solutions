#!/usr/bin/env python3


nums = [1,2]

while nums[-2]+nums[-1] < 4e6:
    nums.append(nums[-2]+nums[-1])

nums = [x for x in nums if x%2 == 0]
print(sum(nums))
