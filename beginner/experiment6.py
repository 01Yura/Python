numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
letters = ["a","b","c","d","e","f"]

print(numbers)
print(letters)

print("------------")

for i in range(len(numbers)):
    print(numbers[i])

print("------------")

for i in range(len(letters)):
    print(letters[i])

print("------------")

for ch in letters:
    print(ch)

print("------------")

print(*numbers)
print(*letters)

print("------------")
string = "Python"
print(*string)
