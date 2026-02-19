from math import log

n = int(input())
x = 0
for i in range(1, n + 1):
    x = x + (1 / i)
print(x - log(n))
