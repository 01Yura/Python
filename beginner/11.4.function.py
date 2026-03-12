num = int(input())
list = []
for i in range(num):
    n = int(input())
    list.append(n ** 2 + 2 * n + 1)
    print(n)
print()
print(*list, sep="\n")
