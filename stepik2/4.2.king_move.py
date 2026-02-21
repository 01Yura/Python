start_str = int(input())
start_col = int(input())
end_str = int(input())
end_col = int(input())

if (start_str == end_str and (
        start_col + 1 == end_col or start_col - 1 == end_col)) or (
        start_col == end_col and (
        start_str + 1 == end_str or start_str - 1 == end_str)):
    print("YES")
elif (end_str == start_str + 1 and (end_col == start_col + 1 or end_col == start_col - 1)) or (
        end_str == start_str - 1 and (end_col == start_col + 1 or end_col == start_col - 1)):
    print("YES")
else:
    print("NO")

str1 = int(input())
col1 = int(input())
str2 = int(input())
col2 = int(input())
if str2 == str1 and (col2 == col1 + 1 or col2 == col1 - 1) or col2 == col1 and (str2 == str1 + 1 or str2 == str1 - 1):
    print('YES')
elif str2 == str1 + 1 and (col2 == col1 + 1 or col2 == col1 - 1) or str2 == str1 - 1 and (
        col2 == col1 + 1 or col2 == col1 - 1):
    print('YES')
else:
    print('NO')
