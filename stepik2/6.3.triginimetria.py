import math

x = float(input())
x = math.radians(x)
z = math.sin(x) + math.cos(x) + pow(math.tan(x), 2)
print(z)
