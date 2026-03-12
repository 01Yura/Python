# объявление функции
def is_valid_password(password):
    password = password.split(":")
    if len(password) != 3:
        return False

    palindrome = password[0]
    simple = int(password[1])
    even = int(password[2])

    # проверяем палиндром
    reversed_palindrome = palindrome[::-1]
    if reversed_palindrome == palindrome:
        if simple > 1:
            # проверяем простоту
            for i in range(2, simple):
                if simple % i == 0:
                    return False
            # проверяем четность
            if even % 2 == 0:
                return True
    else:
        return False

    return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
