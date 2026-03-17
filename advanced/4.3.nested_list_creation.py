# тут 3 варианта создания

n = int(input())
li = []

for i in range(n):
    li.append([j for j in range(1, n + 1)])

print(*li, sep="\n")

print("---------------------")

n = int(input())
result = []

for _ in range(n):
    result.append(list(range(1, n + 1)))

print(*result, sep='\n')

print("---------------------")

n = int(input())
m = int(input())
li = []

for i in range(n):
    li.append([0] * m)

print(*li, sep="\n")
