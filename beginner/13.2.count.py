# объявление функции
def print_symbol_counts(s):
    string = s.lower().strip()
    list_of_chars = list(string)
    unique_list = []
    for el in list_of_chars:
        if el not in unique_list:
            unique_list.append(el)
            unique_list.sort()

    for el in unique_list:
        print(el + ": " + str(list_of_chars.count(el)))


# считываем данные
s = input()

# вызываем функцию
print_symbol_counts(s)
