column1=int(input())
string1=int(input())
column2=int(input())
string2=int(input())
place1, place2 = 'black', 'black'
if column1%2!=0 and string1%2!=0:
    place1='white'
if column2%2!=0 and string2%2!=0:
    place2='white'
if place1==place2:
    print('YES')
else:
    print('NO')
   


col1=int(input())
str1=int(input())
col2=int(input())
str2=int(input())
if (col1+str1)%2==(col2+str2)%2:
  print('YES')
else:
  print('NO')