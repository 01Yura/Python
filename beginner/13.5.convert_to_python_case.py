# объявление функции
def convert_to_python_case(text):
    new_text = ""
    for ch in text:
        if ch.isupper():
            new_text = new_text + "_" + ch.lower()
        else:
            new_text += ch

    return new_text[1::]


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
