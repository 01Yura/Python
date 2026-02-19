from math import *

x = float(input())
x = x * pi / 180
#  sinx+cosx+tan2x
y = sin(x) + cos(x) + pow(tan(x), 2)
print(y)



import math

x=float(input())
x=math.radians(x)
z=math.sin(x)+math.cos(x)+pow(math.tan(x), 2)
print(z)