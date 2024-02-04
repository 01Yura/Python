a, b = int(input()), int(input())
sum = 0
for i in range(a, b + 1):
    for j in range(0, i + 1):
        if i % j == 0:
            sum += j
            max = i
print(max, sum)
