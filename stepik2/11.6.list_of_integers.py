original_list = input().split()
ints = []
for ch in original_list:
    ints.append(int(ch))
ints.sort()
print(*ints)
ints.sort(reverse=True)
print(*ints)