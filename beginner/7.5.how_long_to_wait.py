s = input()
total = 0
i = 0
while s != "Левон":
    total += i
    if s == "Александра":
        i = 1
    s = input()

print(total)
