n = int(input())

summary = 0
while n >= 25:
    total = n // 25
    n = n - (25 * total)
    summary += total
while n >= 10:
    total = n // 10
    n = n - (10 * total)
    summary += total
while n >= 5:
    total = n // 5
    n = n - (5 * total)
    summary += total
while n >= 1:
    total = n // 1
    n = n - (1 * total)
    summary += total

print(summary)




# put your python code here
price = int(input())
counter = 0
while price >= 25:
    price -= 25
    counter += 1
while price >= 10:
    price -= 10
    counter += 1
while price >= 5:
    price -= 5
    counter += 1
while price != 0:
    price -= 1
    counter += 1
print(counter)




