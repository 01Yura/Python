a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a <= b:
    min = a
else:
    min = b
if c <= min:
    min = c
if d <= min:
    min = d
print(min)
