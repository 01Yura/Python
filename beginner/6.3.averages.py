from math import sqrt, pow

a = float(input())
b = float(input())

num1 = (a + b) / 2
num2 = sqrt(a * b)
num3 = 2 * a * b / (a + b)
num4 = sqrt((pow(a, 2) + pow(b, 2)) / 2)
print(num1, num2, num3, num4, sep="\n")
