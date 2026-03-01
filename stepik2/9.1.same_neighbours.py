string = input()
previous = ""
current = ""
counter = 0

for ch in string:
    if ch == previous:
        counter+=1
    previous = ch

print(counter)
