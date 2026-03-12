a = input()
b = input()
c = input()

a_length = len(a)
b_length = len(b)
c_length = len(c)

max = max(a_length, b_length, c_length)
min = min(a_length, b_length, c_length)

if min == a_length:
    print(a)
elif min == b_length:
    print(b)
else:
    print(c)

if max == a_length:
    print(a)
elif max == b_length:
    print(b)
else:
    print(c)
