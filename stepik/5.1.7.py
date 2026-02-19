col1=int(input())
str1=int(input())
col2=int(input())
str2=int(input())
if ((col2==col1-1 or col2==col1+1) and (str2==str1-2 or str2==str1+2)) or ((col2==col1-2 or col2==col1+2) and (str2==str1+1 or str2==str1-1)):
    print('YES')
else:
    print('NO')
    
    
    
    
a1=int(input())
b1=int(input())
a2=int(input())
b2=int(input())
if (a2==a1-2 or a2==a1+2) and (b2==b1-1 or b2==b1+1):
  print('YES')
elif (a2==a1-1 or a2==a1+1) and (b2==b1-2 or b2==b1+2):
  print('YES')
else:
  print('NO')