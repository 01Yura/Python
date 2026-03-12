# объявление функции
def get_next_prime(num):
    for i in range(num + 1, 2 * num + 1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag and i > num:
            return i


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
