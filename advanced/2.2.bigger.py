numbers = input().split()
counter = 0
for i in range(1, len(numbers)):
    if int(numbers[i]) > int(numbers[i - 1]):
        counter += 1
print(counter)
