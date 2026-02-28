n = int(input())

while len(str(n)) != 1:
    total = 0
    for i in range(len(str(n))):
        total += n % 10
        n = n // 10
    n = total
print(n)
