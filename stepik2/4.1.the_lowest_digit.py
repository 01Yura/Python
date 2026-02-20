a = int(input())
b= int(input())
c = int(input())
d = int(input())

if a < b:
    min = a
else:
    min = b
if min > c:
    min = c
if min > d:
    min = d

print(min)