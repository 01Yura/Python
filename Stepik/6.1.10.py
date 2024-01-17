num=int(input())
a=num//100
c=num%10
b=(num//10)%10
num_max=max(a,b,c)
num_min=min(a,b,c)
num_med=a+b+c-num_max-num_min
if num_max-num_min==num_med:
    print('Число интересное')
else:
    print('Число неинтересное')