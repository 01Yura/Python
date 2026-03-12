# объявление функции
def is_correct_bracket(text):
    list_of_brackets = list(text)
    balance = 0
    for ch in list_of_brackets:
        if ch == "(":
            balance += 1
        if ch == ")":
            balance -= 1
        if balance < 0:
            return False

    if balance == 0:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
