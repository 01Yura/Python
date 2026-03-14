n = int(input())
for_print = []
counter = 0
for i in range(n):
    string = input()
    result = list()
    for ch in string:
        if ch == "a" and len(result) == 0:
            result.append(ch)
        elif ch == "n" and (len(result) == 1 or len(result) == 4):
            result.append(ch)
        elif ch == "t" and len(result) == 2:
            result.append(ch)
        elif ch == "o" and len(result) == 3:
            result.append(ch)
    if len(result) == 5:
        counter += 1
        for_print.append(counter)
    else:
        counter += 1
print(*for_print)
