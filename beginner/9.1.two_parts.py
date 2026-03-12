string = input()

if len(string) % 2 == 0:
    first_part = string[:len(string) // 2]
    second_part = string[len(string) // 2:]
else:
    first_part = string[:len(string) // 2 + 1]
    second_part = string[len(string) // 2 + 1:]

print(second_part + first_part)
