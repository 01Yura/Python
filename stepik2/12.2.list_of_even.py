list_1 = input().split()
list_2 = input().split()
list_3 = []

for i in range(len(list_1)):
    list_3.append(int(list_1[i]) + int(list_2[i]))

print(*list_3)
