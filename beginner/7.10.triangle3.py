n = int(input())

for i in range(1, n + 1):
    for j in range(1, i):
        print(j, end="")
    for k in range(i, 0, -1):
        print(k, end="")
    print()
