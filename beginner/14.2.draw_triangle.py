# объявление функции
def draw_triangle():
    for i in range(1, 9):
        for j in range(i, i+1):
            string = " " * int(16//2-i)
            stars = "*" * (i+j-1)
            print(string + stars)


# основная программа
draw_triangle()  # вызов функции
