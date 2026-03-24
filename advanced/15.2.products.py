def print_products(*args):
    counter = 1
    flag = True
    for el in args:
        if type(el) == str and len(el) != 0:
            flag = False
            print(f"{counter}) {el}")
            counter+=1
    if flag:
        print("Нет продуктов")






print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)