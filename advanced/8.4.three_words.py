li = input().split()
result = "YES"

for i in range(1, 3):
    if set(li[i - 1]) == set(li[i]):
        continue
    else:
        result = "NO"
        break
print(result)
