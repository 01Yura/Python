# Сумма цифр = <сумма цифр>
# Произведение цифр = <произведение цифр>

num = int(input())
last_digit = num % 10
second_digit = (num // 10) % 10
first_digit = num // 100

print("Сумма цифр =", first_digit + second_digit + last_digit)
print("Произведение цифр =", first_digit * second_digit * last_digit)