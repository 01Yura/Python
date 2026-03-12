string = input()
new_string = ""
for i in range(len(string)):
    if i % 3 == 0:
        continue
    else:
        new_string += string[i]
        
print(new_string)
