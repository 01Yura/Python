n = int(input())
numbers = list()
for i in range(n):
    numbers.append(int(input()))
product = int(input())
flag = "НЕТ"

for i in range(len(numbers)):
    if flag == "ДА":
        break
    else:
        for j in range(i + 1, len(numbers)):
            if numbers[i] * numbers[j] == product:
                flag = "ДА"
                break
print(flag)
