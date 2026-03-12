num = int(input())

counter = 0
size = len(str(num))
for i in range(1, size + 1):
    digit = num // (10 ** (size - i)) % 10
    if digit % 2 == 0:
        counter+=1
        print(str(counter) + "-я четная цифра равна " + str(digit))

if counter == 0:
    print("Четных цифр в числе нет")
