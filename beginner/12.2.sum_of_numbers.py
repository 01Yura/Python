numbers = input().split()
summary = 0
for i in range(len(numbers)):
    summary += int(numbers[i])
    if i <= len(numbers) - 2:
        print(numbers[i] + "+", end="")

    if i == len(numbers) - 1:
        print(numbers[i] + "=" + str(summary))
