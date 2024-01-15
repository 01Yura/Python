color1=input()
color2=input()
if color1=='красный':
    if color2=='синий':
        print('фиолетовый')
    elif color2=='желтый':
        print('оранжевый')
    elif color2=='красный':
        print('красный')
    else:
        print('ошибка цвета')
elif color1=='синий':
    if color2=='желтый':
        print('зеленый')
    elif color2=='красный':
        print('фиолетовый')
    elif color2=='синий':
        print('синий')
    else:
        print('ошибка цвета')
elif color1=='желтый':
    if color2=='синий':
        print('зеленый')
    elif color2=='красный':
        print('оранжевый')
    elif color2=='желтый':
        print('желтый')
    else:
        print('ошибка цвета')
else:
    print('ошибка цвета')