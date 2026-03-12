from math import pow

a, b = int(input()), int(input())

counter = 0
for i in range(a, b + 1):
    x = pow(i, 3)
    if x % 10 == 4 or x % 10 == 9:
        counter+=1
print(counter)
