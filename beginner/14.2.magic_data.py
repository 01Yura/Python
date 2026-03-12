# объявление функции
def is_magic(date):
    digits = date.split(".")
    last_two = int(digits[2][2] + digits[2][3])
    first = int(digits[0])
    second = int(digits[1])

    return first * second == last_two


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
