# объявление функции
def is_palindrome(text):
    chars = ",.!?- "
    for ch in chars:
        if ch in text:
            text = text.replace(ch, "")
    text = text.lower()
    reversed_text = text[::-1].lower()
    return text == reversed_text


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
