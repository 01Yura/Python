n = int(input())
original_list = list()
list = []
query_list = []

for i in range(n):
    string = input()
    original_list.append(string)
    list.append(string.lower())

k = int(input())
for i in range(k):
    query = input()
    query_list.append(query.lower())

flag = False
for i in range(len(original_list)):
    for qe in query_list:
        if qe in list[i]:
            flag = True
        else:
            flag = False
            break
    if flag:
        print(original_list[i])
