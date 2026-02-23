str1 = input()
str2 = input()
str3 = input()

str1_length = len(str1)
str2_length = len(str2)
str3_length = len(str3)

max = max(str1_length, str2_length, str3_length)
min = min(str1_length, str2_length, str3_length)
med = str1_length + str2_length + str3_length - max - min

if med - min == max - med:
    print("YES")
else:
    print("NO")
