import math
import time

num = float(input())
mlsec = int(input())

time.sleep(mlsec / 1000)

sqrt_num = math.sqrt(num)

print(f"Square root of {num} after {mlsec} miliseconds is {sqrt_num}")