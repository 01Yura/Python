num = int(input())

list_of_strings = list()
for i in range(num):
    list_of_strings.append(input())

new_list = list()
for i in range(len(list_of_strings)):
    for k in range(len(list_of_strings[i])):
        new_list.append(list_of_strings[i][k])

print(new_list)


print("------------------------------")


n = int(input())
seq = []

for _ in range(n):
    s = input()
    seq.extend(s)

print(seq)