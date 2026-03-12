string = input()
max_string = string
min_string = string

while string != "КОНЕЦ":
    if string > max_string:
        max_string = string
    if string < min_string:
        min_string = string
    string = input()

print(f"Минимальная строка ⬇️: {min_string}")
print(f"Максимальная строка ⬆️: {max_string}")
