n = int(input())

string = ""
for i in range(n):
    string+=chr(i+ord("a"))

print(list(string))
