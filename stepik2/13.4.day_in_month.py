# объявление функции
def get_days(month):
    big = [1, 3, 5, 7, 8, 10, 12]
    small = [4, 6, 9, 11]
    if month in big:
        return 31
    elif month in small:
        return 30
    else:
        return 28


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
