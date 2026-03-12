n = int(input())
total = 0
while not (n < 0 or n > 5):
    if n == 5:
        total += 1
    n = int(input())
print(total)
