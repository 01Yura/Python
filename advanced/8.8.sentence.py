sentence = 'Dying for the right cause is the most human thing we can do.'
sentence = sentence.lower()
for ch in ":,.!?();":
    sentence = sentence.replace(ch, "")
list_of_words = sentence.split()

print(*sorted({word for word in list_of_words if len(word) < 4}))
