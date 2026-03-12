number = input()
digits = "1234567890"
flag = "YES"
if number[0] == "7" and number[1] == "-" and len(number) == 14:
    for digit in number[2:5]:
        if digit in digits and number[5] == "-":
            continue
        else:
            flag = "NO"
            break

    for digit in number[6:9]:
        if digit in digits and number[9] == "-":
            continue
        else:
            flag = "NO"
            break

    for digit in number[10:14]:
        if digit in digits:
            continue
        else:
            flag = "NO"
            break

elif len(number) == 12:
    for digit in number[0:3]:
        if digit in digits and number[3] == "-":
            continue
        else:
            flag = "NO"
            break

    for digit in number[4:7]:
        if digit in digits and number[7] == "-":
            continue
        else:
            flag = "NO"
            break

    for digit in number[8:12]:
        if digit in digits:
            continue
        else:
            flag = "NO"
            break
else:
    flag = "NO"

print(flag)
