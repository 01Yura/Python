# Напишите программу, которая с помощью встроенных функций filter(), map(), sorted() и reduce() выводит в алфавитном порядке список primary городов с населением более
# 10000000 человек, в формате:
# Cities: Beijing, Buenos Aires, ...
from functools import reduce

data = [
    ['Sydney', 5367206, 'primary'], ['Perth', 2384371, 'nan'],
    ['Melbourne', 5159211, 'nan'], ['Canberra', 466566, 'admin'],
    ['Darwin', 127532, 'nan'], ['Jakarta', 41913860, 'admin'],
    ['Kolkata', 22549738, 'primary'], ['Shenzhen', 13878396, 'primary'],
]

data = list(filter(lambda x: x[2] == 'primary' and x[1] > 10000000, data))
print(data)
data = list(map(lambda x: x[0], data))
data.sort()
print(data)
data = reduce(lambda x, y: x + y + ", " , data, "Cities: ")
print(data[:-2])