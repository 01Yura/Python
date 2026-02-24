n = int(input())

largest = 0
second_largest = 0
for i in range(n):
    num = int(input())
    if num > largest:
        second_largest = largest
        largest = num
    elif num < largest and num > second_largest:
        second_largest = num

print(largest)
print(second_largest)
