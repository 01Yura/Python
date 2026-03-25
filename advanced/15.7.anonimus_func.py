# преобразует список floats в список чисел, возведенных в квадрат и округленных с точностью до одного десятичного знака
# фильтрует список words и оставляет только палиндромы длиной более 4 символов
# находит произведение чисел из списка numbers
from functools import reduce

floats = [7.6, 15.4, 8.9, -5.6, 42.1]
words = ['pop', 'level', 'python', 'huh']
numbers = [4, -8, 5, 12, -85]

floats = list(map(lambda x: round(x ** 2, 1), floats))
words = list(filter(lambda x: len(x) > 4 and x == x[::-1], words))
total = reduce(lambda x, y: x * y, numbers)

print(floats)
print(words)
print(total)
