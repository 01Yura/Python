numbers = [4.12, 1.3257, 9.37037, 4.552, 3.186]

def new_round(num):
    return round(num, 2)

print(*map(new_round, numbers), sep="\n")


