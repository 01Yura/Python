numbers = input()
original_length = len(numbers)

my_set = set(numbers)
set_length = len(my_set)

if original_length == set_length:
    print("YES")
else:
    print("NO")
