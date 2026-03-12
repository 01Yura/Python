num = int(input())
list = list()
for i in range(num):
    list.append(input())

k = int(input())
for i in range(len(list)):
    if len(list[i]) >= k:
     print(list[i][k-1], end="")
