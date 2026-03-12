# объявление функции
def get_unique(numbers):
    unique_list = []
    for el in numbers:
        if el not in unique_list:
            unique_list.append(el)
    return unique_list


# считываем данные
numbers = eval(input())

# вызываем функцию
print(get_unique(numbers))
