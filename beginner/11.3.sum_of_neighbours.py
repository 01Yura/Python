num = int(input())
list = []
previous_number = 0

for i in range(num):
    sum = 0
    current_number = int(input())
    sum = previous_number + current_number
    list.append(sum)
    previous_number = current_number

del list[0]
print(list)
