from functools import reduce

file = open(input())
content = file.readlines()
total = reduce(lambda x, y: int(x) + int(y), content)
print(total)