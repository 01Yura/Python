# Квадрат числа <текущее число> равен <квадрат текущего числа>
from math import pow

n = int(input())

for i in range(n+1):
    print("Квадрат числа", i, "равен", int(pow(i,2)))