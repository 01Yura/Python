list_of_words = input().split(".")
flag = "ДА"
for el in list_of_words:
    if 0 <= int(el) <= 255:
        continue
    else:
        flag = "НЕТ"
        break
print(flag)
