n=int(input())
d=n%10
c=n//10%10
b=n//100%10
a=n//1000
print("Цифра в позиции тысяч равна", a)
print("Цифра в позиции сотен равна", b)
print("Цифра в позиции десятков равна", c)
print("Цифра в позиции единиц равна", d)



num=int(input())
a=num//1000
b=(num%1000)//100
c=(num%100)//10
d=num%10
print('Цифра в позиции тысяч равна', a)
print('Цифра в позиции сотен равна', b)
print('Цифра в позиции десятков равна', c)
print('Цифра в позиции единиц равна', d)