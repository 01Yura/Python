a = 1
b = 2
c = a + b
print(c)

num1 = num2 = 5
print(num1, num2)

num_1, num_2 = 5, 7
print(num_1, num_2)


swap1 = 8
swap2 = 9
print(swap1, swap2)

swap1, swap2 = swap2, swap1

swap1, swap2 = swap2, swap1 + swap2
print(swap1, swap2)

swap2 -= c
print(swap2)

a, *b, c = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)
