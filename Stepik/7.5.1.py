num = int(input())
while num != 0:
    last_digit = num % 10
    num //= 10
    print(last_digit)



n = int(input())
while n > 0:
    print(n % 10)
    n //= 10