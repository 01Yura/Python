num = int(input())
reversed_num = ""

while num != 0:
    last_digit = num % 10
    reversed_num += str(last_digit)
    num //= 10

print(reversed_num)
