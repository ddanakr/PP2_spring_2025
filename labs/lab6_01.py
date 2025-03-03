"""
nums = [1,2,3,4,5,6]

prod = 1

for num in numbers:
    prod *= num

print(prod)
"""

from functools import reduce

nums = [1,2,3,4,5,6]

prod = reduce(lambda x,y: x * y, nums)

print(prod)
