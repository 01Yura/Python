numbers = [12, 2, -30, 48, 51, -60, 19, 10, 13]

def is_greater10(num):  # функция возвращает значение True если число больше 10 и False в противном случае
    return num > 10

large_numbers = filter(is_greater10, numbers)  #  список large_numbers содержит элементы, большие 10

print(*large_numbers)