num = int(input())

list = []
for _ in range(num):
    n = int(input())
    list.append(n)
result = []
for i in range(len(list)):
    if i % 2 == 0:
        result.append(list[i])
print(result)
