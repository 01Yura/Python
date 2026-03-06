a, b, c = input(), input(), input()

max_word = max(a, b, c)
min_word = min(a, b, c)
middle_word = ""

if a == max_word:
    if b == min_word:
        middle_word = c
    else:
        middle_word = b
elif b == max_word:
    if c == min_word:
        middle_word = a
    else:
        middle_word = c
elif c == max_word:
    if b == min_word:
        middle_word = a
    else:
        middle_word = b

print(min_word, middle_word, max_word)
