# объявление функции
def is_password_good(password):
    validation_factor_1 = False
    validation_factor_2 = False
    validation_factor_3 = False

    if len(password) >= 8:
        for ch in password:
            if ch == ch.upper() and not ch.isdigit():
                validation_factor_1 = True
                break
        for ch in password:
            if ch == ch.lower() and not ch.isdigit():
                validation_factor_2 = True
                break
        for ch in password:
            if ch.isdigit():
                validation_factor_3 = True
                break

    else:
        return False

    if validation_factor_1 and validation_factor_2 and validation_factor_3:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
