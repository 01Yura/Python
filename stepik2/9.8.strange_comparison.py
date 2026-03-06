a, b = input(), input()

a = a.lower()
b = b.lower()
new_a = ""
new_b = ""

for i in range(len(a)):
    if a[i].isalpha():
        new_a += a[i]

for i in range(len(b)):
    if b[i].isalpha():
        new_b += b[i]

if new_a == new_b:
    print("YES")
else:
    print("NO")
