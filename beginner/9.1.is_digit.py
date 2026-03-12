string = input()

flag = False
for ch in string:
    if ch in "1234567890":
        print("Цифра")
        flag = True
        break
if not flag:
    print("Цифр нет")
