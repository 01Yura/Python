from math import pow, sqrt

a, b, c = float(input()), float(input()), float(input())
d = pow(b, 2) - 4 * a * c
if d == 0:
    x = -b / (2 * a)
    print(x)
elif d < 0:
    print('Нет корней')
else:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    max1 = max(x1, x2)
    min1 = min(x1, x2)
    print(min1, max1, sep='\n')
