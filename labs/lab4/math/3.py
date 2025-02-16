import math
n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))

degree = 180 / n
radian = degree * (math.pi / 180)

area = (n * a**2) / (4 * math.tan(radian))

print(round(area))