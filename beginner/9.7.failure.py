string = input()

while True:
    start_index = string.find("[")

    if start_index >= 0:
        end_index = string.find("]")
        diget = string[start_index + 3:end_index]
        letter = chr(int(diget))
        string = string.replace(string[start_index: end_index + 1], letter)
    else:
        break
print(string)
