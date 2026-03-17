words = ['summer', 'city', 'Earth', 'peace', 'kindness', 'Dog', 'turtle']
print(*sorted({word[0].lower() for word in words}))