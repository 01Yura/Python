n = int(input())
li = list()
for i in range(n):
    li.append(input())

se = set(li[0])
for i in range(1,len(li)):
    se = se.intersection(set(li[i]))
print(*sorted(se))