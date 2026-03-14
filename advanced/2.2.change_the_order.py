original = input().split()
odd = [original[i] for i in range(len(original)) if i % 2 != 0]
even = [original[i] for i in range(len(original)) if i % 2 == 0]
new_list = []
for i in range(len(original) // 2):
    new_list.append(odd[i])
    new_list.append(even[i])
if len(original) % 2 != 0:
    new_list.append(original[len(original) - 1])

print(*new_list)
