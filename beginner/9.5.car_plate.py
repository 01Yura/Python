plate = input()

letters = "АВЕКМНОРСТУХ"
numbers = "0123456789"

flag = False
if "_" in plate:
    index = plate.find("_")
    last_part = plate[index + 1:]
    if 2 <= len(last_part) <= 3 and last_part.isnumeric():
        if plate[0] in letters:
            if plate[1:4].isnumeric():
                for ch in plate[5:7]:
                    if ch in letters:
                        flag = True
                    else:
                        flag = False
                    break
if flag:
    print("YES")
else:
    print("NO")
