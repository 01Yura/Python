a, b = int(input()), int(input())
maxtotal=0
for i in range(a, b + 1):
    total=0
    for divisor in range (1, i+1):
        if i%divisor==0:
            total+=divisor
        if total>=maxtotal:
            maxtotal=total
            digit=i
print(digit, maxtotal)