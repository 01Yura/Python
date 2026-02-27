a, b = int(input()), int(input())

for i in range(a, b + 1):
    if i == 1:
        continue
    for j in range(2, i + 1):
        flag = True
        if i % j == 0 and i != j:
            flag = False
            break
    if flag:
        print(i)
