from math import tan, radians

n, a = int(input()), float(input())
p = a * n
A = a / (2 * tan(radians(180) / n))
s = p * A / 2
print(s)
