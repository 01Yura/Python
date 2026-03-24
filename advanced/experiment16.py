import time

li1 = [13, 2, 3, 4, 5]
li2 = [6, 7, 8, 0.99]
li3 = [10, 11, 12]
print(sorted(li2, key=len()))

print(max(max(li1), max(max(li2), max(li3))))


def find_nod(a, b):
    """
    Some text
    :param a: first
    :param b: second
    :return: result
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


print(find_nod(18, 24))

help(sorted)


