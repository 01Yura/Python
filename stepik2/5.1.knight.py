col1 = int(input())
str1 = int(input())
col2 = int(input())
str2 = int(input())

if ((col2 == col1 - 1 or col2 == col1 + 1) and (str2 == str1 - 2 or str2 == str1 + 2)) or (
        (col2 == col1 - 2 or col2 == col1 + 2) and (str2 == str1 + 1 or str2 == str1 - 1)):
    print('YES')
else:
    print('NO')
