from functools import reduce

numbers = [7, 5, -4, 0, 3, -5, 6, 7, 15]


def square(x):
    return x ** 2

def add(x, y):
    return x+y

print(reduce(add, map(square, numbers), 0))
