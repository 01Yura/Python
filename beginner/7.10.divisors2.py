a, b = int(input()), int(input())
maximum = 0
current = 0
total_maximum = 0

for i in range(a, b + 1):
    total_current = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total_current += j
    if total_current >= total_maximum:
        total_maximum = total_current
        maximum = i
print(maximum, total_maximum)
