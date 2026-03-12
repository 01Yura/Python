string = input()

sum = 0
for ch in string:
    amount = ord(ch) * 3
    sum += amount
print("Текст сообщения:", "'" + string + "'")
print("Стоимость сообщения:", str(sum) + "🐝")
