list_of_numbers = input().split()
counter = 0
for i in range(len(list_of_numbers)):
    for j in range(i+1, len(list_of_numbers)):
        if list_of_numbers[i] == list_of_numbers[j]:
            counter += 1
print(counter)
