digital = "Helloo"
print(digital[0], digital[-1:-6:-1], sep='')

num = "123456789"
num = num[-3:]
print(num)

num = "123456789"
num = num[:len(num)-3]
print(num)

print('{:,}'.format(1234567890))