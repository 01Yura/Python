# при n = 4, получится:
# [1]
# [1, 2]
# [1, 2, 3]
# [1, 2, 3, 4]
# тут 2 варианта создания

n = int(input())
li = list()

for i in range(1, n + 1):
    li.append(list(range(1, i + 1)))

print(*li, sep="\n")

print("-----------------")

n = int(input())
li = list()

for i in range(1, n + 1):
    li.append([i for i in range(1, i + 1)])

print(*li, sep="\n")
