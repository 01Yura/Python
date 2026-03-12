string = input()
counter = 0

lowers = "qwertyuioplkjhgfdsazxcvbnm"
for ch in string:
    if ch in lowers:
        counter += 1
print(counter)



# this option(variant) is better
s = input()
counter = 0
for i in range(len(s)):
    if s[i] != s.upper()[i]:
        counter += 1
print(counter)



s = input()
counter = 0
for char in s:
    if char != char.upper():  # условие выполняется только для букв в нижнем регистре
        counter += 1
print(counter)
