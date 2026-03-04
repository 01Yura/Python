nickname = input()

flag = False
if nickname.startswith("@"):
    if 5 <= len(nickname) <= 15:
        if nickname[1:].isalnum():
            if nickname[1:].islower() or nickname[1:].isnumeric():
                flag = True
if flag:
    print("Correct")
else:
    print("Incorrect")
