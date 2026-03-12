num = int(input())
list = []

for i in range(num):
    n = int(input())
    list.append(n)

for el in list:
    if el < 0:
        print(el)

for el in list:
    if el == 0:
        print(el)

for el in list:
    if el > 0:
        print(el)
