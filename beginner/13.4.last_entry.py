# объявление функции
def get_last_index(data: list, value):
    data.reverse()
    if value in data:
        return len(data) - data.index(value) - 1
    else:
        return "ERROR!"


# считываем данные
data = eval(input())
value = eval(input())

# вызываем функцию
print(get_last_index(data, value))
