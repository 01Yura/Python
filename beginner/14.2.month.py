# объявление функции
def get_month(language, number):
    list_in_english = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                       'november', 'december']
    list_in_russian = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
                       'ноябрь', 'декабрь']

    if language == "ru":
        return list_in_russian[number - 1]
    else:
        return list_in_english[number - 1]


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
