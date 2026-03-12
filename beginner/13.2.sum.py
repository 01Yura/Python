# объявление функции
def print_digit_sum(num):
    summary = 0
    while num != 0:
        last = num % 10
        summary +=last
        num = num // 10
    print(summary)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)