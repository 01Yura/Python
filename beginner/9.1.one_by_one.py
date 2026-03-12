string = input()

for i in range(len(string)):
    print(str(i + 1) + ") " + string[i])

print("-------------------------------")
position = 0
for ch in string:
    position += 1
    print(str(position) + ") " + ch)
