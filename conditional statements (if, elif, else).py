x=0

if x == 0:
    x = 1
    print('x был равен нулю')
elif type(x) == type(5) or type(x) == type(5.5):
    print('x имеет допустимое значение')
else:
    x=1
    print('В x недопустимое значение')
print(100/x)

##    

x=int(input('Enter a number: '))

if x == 0:
    print('if')
elif x > 0:
    print('elif')
else:
    print('else')

##

x=int(input('Enter a number: '))
if x == 0:
    x += 1
print(10/x)

##

