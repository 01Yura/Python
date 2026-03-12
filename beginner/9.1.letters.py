s = input()
vowels = 'ауоыиэяюёеяАУОЫТЭЯЮЕЁЯ'
count_v = 0
consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗКЛМНПРСТФКЦЧШЩ'
count_c = 0

for c in s:
    if c in vowels:
        count_v += 1
    if c in consonants:
        count_c += 1
print('Количество гласных букв равно', count_v)
print('Количество согласных букв равно', count_c)
