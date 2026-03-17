poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
spisok = list(poet_data)[:-1]
spisok.append('Москва')
poet_data = tuple(spisok)

print(poet_data)