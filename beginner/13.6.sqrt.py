from math import pow, sqrt


# объявление функции
def solve(a, b, c):
    d = pow(b, 2) - 4 * a * c
    if d == 0:
        x = -b / (2 * a)
        return x, x
    else:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        max1 = max(x1, x2)
        min1 = min(x1, x2)
        return min1, max1


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
