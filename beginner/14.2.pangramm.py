# объявление функции
def is_pangram(text):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    for ch in letters:
        if ch not in text.lower() and ch != " ":
            return False
    return True


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
