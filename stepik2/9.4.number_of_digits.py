string = input()

counter = 0
for ch in string:
    if ch in "1234567890":
        counter += 1
print(counter)
