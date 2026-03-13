n = input()
result = ""
if len(n) < 5:
    print(n)
else:
    while len(n) > 2:
        part = n[-3:]
        result = part + "," + result
        n = n[:len(n) - 3]
    result = result[:-1]
    result = n + "," + result
    if result[0] == ",":
        result = result[1:]
    print(result)
