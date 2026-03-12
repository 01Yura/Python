num = int(input())

flag = 'YES'
last_digit = num % 10
while num != 0:
    current_digit = last_digit
    last_digit = num % 10
    if current_digit == last_digit:
        num //= 10
    else:
        flag = 'NO'
print(flag)
