# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение:
# сумма первой и последней цифр равна разности второй и третьей цифр.

num = int(input())
fourth_digit = num % 10
third_number = num // 10 % 10 # 1234 // 10 = 123 % 10 = 3
second_number = num // 100 % 10 # 1234 // 100 = 12 % 10 = 2
first_digit = num //1000

if first_digit + fourth_digit == second_number - third_number:
    print("ДА")
else:
    print("НЕТ")