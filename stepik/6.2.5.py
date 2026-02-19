str1=input()
str2=input()
str3=input()
a=len(str1)
b=len(str2)
c=len(str3)
min1=min(a, b, c)
max1=max(a, b, c)
if min1==a:
  a1=a
elif min1==b:
  a1=b
else:
  a1=c
if max1==a:
  a3=a
elif max1==b:
  a3=b
else:
  a3=c
a2=a+b+c-a1-a3
if a3-a2==a2-a1:
  print('YES')
else:
  print('NO')