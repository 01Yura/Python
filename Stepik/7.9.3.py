a, b = int(input()), int(input())
summa = 0
for i in range(a, b + 1):
    summa1 = summa
    summa = 0
    for j in range(1, i + 1):
        if i % j == 0:
            summa += j
    if summa1 <= summa:
        maxsumma = summa
        maxdigit = i
print(maxdigit, maxsumma)
