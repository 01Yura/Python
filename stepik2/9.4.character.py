string = input()
ch = 0
max = 0
symbol = string[0]

for i in range(len(string)):
    current = 0
    for ch in string:
        current = string.count(ch)
        if current >= max:
            max = current
            symbol = ch
print(symbol)
