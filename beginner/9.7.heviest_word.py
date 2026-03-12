max = 0
heaviest_word = ""
for i in range(4):
    word = input()
    sum = 0
    for ch in word:
        sum += ord(ch)
    if sum > max:
        max = sum
        heaviest_word = word
print(heaviest_word)
