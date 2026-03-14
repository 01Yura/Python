string = input()
maximum = 0
if "Р" in string:
    counter = 0
    for i in range(1, len(string)):
        if string[i] == "Р" and string[i] == string[i - 1]:
            counter += 1
            if counter > maximum:
                maximum = counter
        else:
            counter = 0
    print(maximum + 1)
else:
    print(0)
