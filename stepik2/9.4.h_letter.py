string = input()

first_index = string.find("h")
second_index = string.rfind("h")
removed = string[first_index:second_index + 1]
print(string.replace(removed, ""))
