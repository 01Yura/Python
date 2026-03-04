letter = input()

if letter == "Я":
    print("Дальше букв нет")
else:
    next_letter = chr(ord(letter) + 1)
    print(next_letter)