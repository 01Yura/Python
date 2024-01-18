from math import *

a, b = float(input()), float(input())
y1 = (a + b) / 2
y2 = sqrt(a * b)
y3 = 2 * a * b / (a + b)
y4 = sqrt((pow(a, 2) + pow(b, 2)) / 2)
print(y1, y2, y3, y4, sep='\n')
