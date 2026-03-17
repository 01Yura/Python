n = int(input())
se = set()

for i in range(n):
    string = input().lower()
    for ch in string:
        se.add(ch)

print(len(se))
