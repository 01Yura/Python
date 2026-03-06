string = input()

first_index = string.find("h")
second_index = string.rfind("h")
piece = string[first_index + 1:second_index]
reversed_piece = piece[::-1]
print(string[:first_index + 1] + reversed_piece + string[second_index:])
