n = int(input())
list_of_digits = []
for i in range(n):
    list_of_digits += [int(digit) for digit in input().split()]


def quick_merge(list1):
    list1.sort()
    return list1


result = quick_merge(list_of_digits)
print(*result)
