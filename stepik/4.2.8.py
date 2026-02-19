str1=int(input())
col1=int(input())
str2=int(input())
col2=int(input())
if str2==str1 and (col2==col1+1 or col2==col1-1) or col2==col1 and (str2==str1+1 or str2==str1-1):
    print('YES')
elif str2==str1+1 and (col2==col1+1 or col2==col1-1) or str2==str1-1 and (col2==col1+1 or col2==col1-1): 
    print('YES')
else:
    print('NO')
    

  
    
str1=int(input())
col1=int(input())
str2=int(input())
col2=int(input())
if (str2==str1 or str2==str1-1 or str2==str1+1) and (col2==col1 or col2==col1-1 or col2==col1+1):
  print('YES')
else:
  print('NO')