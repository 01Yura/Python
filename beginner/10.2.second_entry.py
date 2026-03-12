string = input()

counter = 0
first_entry = -1
if string.find("f") != -1:
    first_entry = string.find("f")
    counter += 1
if string.find("f", first_entry + 1) != -1 and string.find("f", first_entry + 1) != string.find("f"):
    counter += 1
    index = string.find("f", first_entry + 1)
    print(index)
else:
    if counter == 0:
        print("-2")
    else:
        print("-1")
