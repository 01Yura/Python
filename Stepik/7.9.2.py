n = int(input())
for i in range(1, n + 1):
    count1 = 0
    for k in range(i):
        count1 += 1
        print(count1, end="")
    for j in range(count1 - 1, 0, -1):
        print(j, end="")
    print()


n = int(input())
for i in range(1, n + 1):
    count = 0
    for k in range(i):
        count += 1
        print(count, end="")
    for j in range(i, 1, -1):
        count -= 1
        print(count, end="")
    print()
