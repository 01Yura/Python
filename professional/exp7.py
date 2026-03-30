letters = ['a', 'b', 'c']

letters[2:6] = ['d', 'e', 'f']
print(letters)

print("---------------")
my_set = set()

for i in range(3):
    my_set.add(i + 1)
    my_set.discard(i - 1)

print(my_set)
print(len(my_set))


print("---------------")

x = 10
my_dict = {'Timur': x, 'Ruslan': x, 'Anri': x}
x = 11

print(my_dict['Timur'])

print("---------------")

def word_dict(word):
    d = {}
    for c in word:
        d[c] = d.get(c, 0) + 1
    return d


x = word_dict('BEEgeek')['e']

print(x)