a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a2>b1 or a1>b2:
  print('пустое множество')
elif a2>a1:
    if b1==a2:
        print(b1)
    elif b2>=b1:
        print(a2, b1)
    elif b2<b1:
        print(a2, b2)
elif a2<a1:
    if b2==a1:
        print(b2)
    elif b2>=b1:
        print(a1, b1)
    elif b2<b1:
        print(a1, b2)
    elif a1==b2:
        print(a1)
elif a1==a2:
    if b2>=b1:
        print(a1, b1)
    elif b2<b1:
        print(a1, b2)