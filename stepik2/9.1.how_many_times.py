string = input()

plus = 0
star = 0
for ch in string:
    if ch == "+":
        plus += 1
    elif ch == "*":
        star += 1

print("Символ + встречается", plus, "раз")
print("Символ * встречается", star, "раз")
