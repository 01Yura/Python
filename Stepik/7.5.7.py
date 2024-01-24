num = int(input())
flag = "YES"
penultimate_digit = num % 10
num = num // 10
while not num == 0:
    last_digit = penultimate_digit
    penultimate_digit = num % 10
    num //= 10
    if penultimate_digit < last_digit:
        flag = "NO"
print(flag)


n = int(input())
flag = "YES"
y = 0
counter = 0
while n > 0:
    counter += 1
    last = n % 10
    n = n // 10
    if (last != 0 and last >= y) or (last == 0 and counter == 1):
        y = last
    else:
        flag = "NO"
print(flag)
