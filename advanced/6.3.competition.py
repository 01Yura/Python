n = int(input())

result = list()
for i in range(n):
    li = input().split()
    result.append(li)

for el in result:
    print(*el)

print()

for el in result:
    if 4 <= int(el[1]) <= 5:
        print(*el)


n = int(input())

result = list()
for i in range(n):
    li = input().split()
    result.append(tuple(li))

for el in result:
    print(*el)

print()

for el in result:
    for name, grade in el:
        if int(grade) > 3:
            print(name, grade)