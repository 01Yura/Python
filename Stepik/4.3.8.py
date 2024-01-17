a=int(input())
g='зеленый'
r='красный'
b='черный'
if 0<=a<=36:
  if a==0:
    print(g)
  elif 1<=a<=10 or 19<=a<=28:
    if a%2==0:
      print(b)
    else:
      print(r)
  elif 11<=a<=18 or 29<=a<=36:
    if a%2==0:
      print(r)
    else:
      print(b)
else:
  print('ошибка ввода')