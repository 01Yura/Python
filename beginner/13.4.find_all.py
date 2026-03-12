# объявление функции
def find_all(target, symbol):
    indices = []
    for i in range(len(target)):
        if target[i] == symbol:
            indices.append(i)
    return indices


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
