n = int(input())

for i in range(1, n + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += 1
    print(str(i) + "+" * total)
