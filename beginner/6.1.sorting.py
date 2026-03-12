a = int(input())
b = int(input())
c = int(input())

max = max(a, b, c)
min = min(a, b, c)
med = a + b + c - max - min

print(max)
print(med)
print(min)
