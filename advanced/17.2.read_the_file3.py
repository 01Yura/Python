from random import choice


def get_random_string(filename):
    file = open(filename)
    lines = file.readlines()
    random_line = choice(lines)
    file.close()
    return random_line.rstrip()


print(get_random_string("animals1.txt"))