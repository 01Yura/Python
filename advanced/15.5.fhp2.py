numbers = [854, 10, 5, 452, 478, 236, 202, 41]


def cube(x):
    return int(x) ** 3


def predicate(x):
    return x % 5 == 2 and len(str(x)) == 3


print(*map(cube, list(filter(predicate, numbers))), sep="\n")
