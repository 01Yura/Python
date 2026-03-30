from datetime import date, time

l = input('Введите дату в формате ДД.ММ.ГГГГ\n').split('.')
day, month, year = l
# hour, minute, second = input('Введите время в формате ЧЧ:ММ:СС\n').split(':')

my_date = date(int(year), int(month), int(day))        # создаем объект типа date
# my_time = time(int(hour), int(minute), int(second))    # создаем объект типа time

print(my_date)
# print(my_time)