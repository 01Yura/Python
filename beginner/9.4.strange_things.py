num = int(input())
counter = 0

for i in range(num):
    string = input()
    x = string.count("11")
    if x >= 3:
        counter += 1
print(counter)
