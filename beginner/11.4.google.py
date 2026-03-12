n = int(input())
original_list = list()
list = []

for i in range(n):
    string = input()
    original_list.append(string)
    list.append(string.lower())

query = input().lower()

for i in range(len(list)):
    if query in list[i]:
        print(original_list[i])
