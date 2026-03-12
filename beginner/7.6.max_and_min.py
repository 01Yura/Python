n = int(input())
maximum = 0
minimum = 9

while n != 0:
    last_digit = n % 10
    n //= 10
    if last_digit > maximum:
        maximum = last_digit
    if last_digit < minimum:
        minimum = last_digit

print("Максимальная цифра равна", str(maximum))
print("Минимальная цифра равна", str(minimum))
