# объявление функции
def print_case_counts(s):
    upper_case_counter = 0
    lower_case_counter = 0
    for ch in s:
        if ch.isalpha():
            if ch == ch.upper():
                upper_case_counter+=1
            elif ch == ch.lower():
                lower_case_counter+=1
        else:
            continue
    print(f"Букв в верхнем регистре: {upper_case_counter}")
    print(f"Букв в нижнем регистре: {lower_case_counter}")

# считываем данные
s = input()

# вызываем функцию
print_case_counts(s)