x=0

while x<5:
    x+=1
    print(x)


while True:
    x=int(input('Введите число: '))
    count=0
    y=1
    while count<x:
        count +=1
        y*=count
    else:
        print(y)
