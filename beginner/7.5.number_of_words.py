s = input()
counter = 0
while not (s == "стоп" or s == "хватит" or s == "достаточно"):
    counter += 1
    s = input()
print(counter)
