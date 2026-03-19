from decimal import Decimal as D

d = D(input())
li = list()
for ch in str(d):
    if ch in "1234567890":
        li.append(int(ch))
print(max(li) + min(li))
