original_list = input().split()
ints = []
for ch in original_list:
    ints.append(int(ch))
max_digit = max(ints)
min_digit = min(ints)

max_index = ints.index(max_digit)
min_index = ints.index(min_digit)

ints[max_index] = min_digit
ints[min_index] = max_digit

print(*ints)
