num1=int(input())
num2=int(input())
sign=input()
if sign=='+':
    print(num1+num2)
elif sign=='-':
    print(num1-num2)
elif sign=='*':
    print(num1*num2)
elif sign=='/' and num2!=0:
    print(num1/num2)
else:
    print('Неверная операция')