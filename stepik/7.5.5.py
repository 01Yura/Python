num = int(input())
while len(str(num)) != 1:
    last_digit = num % 10
    num //= 10
print(last_digit)


n = int(input())
while n > 99:
    n //= 10

second_digit = n % 10
print(second_digit)
