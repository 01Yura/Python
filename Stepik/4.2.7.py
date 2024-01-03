str1=int(input())
col1=int(input())
str2=int(input())
col2=int(input())
if (str1==str2 and (col1==col2+1 or col1==col2-1)) or (col1==col2 and (str1==str2+1 or str1==str2-1)) or (str1==str2+1 or str1==str2-1) or ((col1+1==col2 and (str1+1==str2 or str1-1==str2)) or (col1-1==col2 and (str1+1==str2 or str1-1==str2))):
    print('YES')
else:
    print('NO')
    
    
    
str1=int(input())
col1=int(input())
str2=int(input())
col2=int(input())
if str2==str1 or col2==col1:
  print('YES')
else:
  print('NO')
