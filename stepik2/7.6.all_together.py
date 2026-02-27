num = int(input())

summary = 0
counter = 0
product = 1
average = 0
first_digit = (num // (10 ** (len(str(num))-1)))
last_digit = num % 10

while num != 0:
    counter+=1
    current_digit = num % 10
    summary+=current_digit
    product*=current_digit
    num //= 10

average = summary / counter
summary_first_and_last = first_digit + last_digit

print(summary)
print(counter)
print(product)
print(average)
print(first_digit)
print(summary_first_and_last)


