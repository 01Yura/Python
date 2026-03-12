num = int(input())
list = []
for i in range(num):
    string = input()
    if string not in list:
        list.append(string)

print(*list, sep="\n")
