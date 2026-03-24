numbers = [(-1, 2), (3, 14), (5, 6, 9)]


def avg(pair):
    length = len(pair)
    return sum(pair) / length


def show_min_and_max(pairs, key=avg):
    print(min(pairs, key=key))
    print(max(pairs, key=key))


show_min_and_max(numbers)

rub = 10
kop = 99
print("I have %s and %s"%(rub, kop))
print(f"I have {rub} and {kop}")
print("I have {1} and {0}".format(rub, kop))

