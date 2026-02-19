num = int(input())
total = 0  # sum
counter = 0  # amount of digits
product = 1
while num != 0:
    last_digit = num % 10
    num //= 10
    total += last_digit
    product *= last_digit
    counter += 1
    if counter == 1:
        last_digit_2 = last_digit
    if len(str(num)) == 1:
        first_digit = last_digit
average = total / counter
sum2 = last_digit_2 + first_digit
print(total, counter, product, average, first_digit, sum2, sep="\n")

n = int(input())
sum = 0
prod = 1
counter = 0
while n != 0:
    if len(str(n)) == 1:
        first = n
    counter += 1
    x = n % 10
    if counter == 1:
        last = x
    n = n // 10
    sum += x
    prod *= x

print(sum, counter, prod, sum / counter, first, first + last, sep="\n")
