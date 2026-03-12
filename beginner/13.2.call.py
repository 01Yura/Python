# объявление функции
def print_perm_time_call(msc_time):
    time_list = msc_time.split(":")
    hours = int(time_list[0])
    minutes = time_list[1]
    hours += 2
    if len(str(hours)) < 2:
        hours = "0" + str(hours)
    print(f"Созвон будет в {hours}:{minutes}.")


# считываем данные
msc_time = input()

# вызываем функцию
print_perm_time_call(msc_time)
