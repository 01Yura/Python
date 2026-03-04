string = input()

counter = string.count("f")
if counter == 0:
    print("NO")
else:
    if counter == 1:
        print(string.find("f"))
    else:
        print(string.find("f"), string.rfind("f"))
