file = open(input())
for line in file:
    print(line.rstrip())
file.close()

file = open(input())
print(file.read())
file.close()

file = open(input())
print(*file.readlines())
file.close()