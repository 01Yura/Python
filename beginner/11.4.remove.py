n = int(input())

list = []
for i in range(n):
    num = int(input())
    list.append(num)

maximum = max(list)
minimum = min(list)

max_index = 0
min_index = 0
for i in range(len(list)):
    if list[i] == maximum:
        del list[i]
        break

for i in range(len(list)):
    if list[i] == minimum:
        del list[i]
        break

print(*list, sep="\n")
