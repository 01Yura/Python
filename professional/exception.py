try:
    num1 = int(input())
    num2 = int(input())
    print('Частное чисел равно', num1 / num2)
except ValueError:
    print('Нужно было ввести числа!')
except ZeroDivisionError:
    print('На ноль делить нельзя!')

print('Работа программы завершена!')