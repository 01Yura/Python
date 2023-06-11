x=''
while len(x)<5:
    y=input('Enter data: ')
    x+=y
else:
    print(x)



x=''
while len(x)<5:
    y=input('Enter data: ')
    if y=='o':
        continue #прерывает цикл на данном моменте и запускает снова
    if y=='l':
        break #полностью прерывает цикл на данном этапе
    x+=y 
else:
    print(x)

print('Работаем')
