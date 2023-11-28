n = int(input())  # Школьники
k = int(input())  # Мандарины
a = k // n  # Количество целых мандаринов для каждого школьника
b = k % n  # Остаток целых мандаринов
print(a)
print(b)

sh=int(input())
m=int(input())
print(m//sh, m%sh, sep="\n")