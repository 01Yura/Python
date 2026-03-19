from decimal import Decimal as D

s = '0.0 5.42 8.63 10.25 1.6 -8.5 -13.0'
li = [D(num) for num in s.split()]
print(li)
print(sum([max(li), min(li)]))
