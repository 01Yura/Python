files = ['pygen_icon.png', 'Oppenheimer(2024).mkv', 'ideas.TxT', 'codes.txt', 'avatar.PNG']
print(*sorted({word.lower() for word in files if word[-3:].lower() == "png"}))