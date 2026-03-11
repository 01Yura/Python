# объявление функции
def print_sorted_hyphen(s):
    words = s.split("-")
    words.sort()
    print(*words, sep="-")


# считываем данные
s = input()

# вызываем функцию
print_sorted_hyphen(s)
