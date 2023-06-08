#class 'NoneType'#
a=None
print(type(a))

#class 'int'#
a=1
print(type(a))

#class 'float'#
a=5.5
print(type(a))

#class 'str'#
a="Hello"
print(type(a))

#class 'list'#
a=[1, 2, "xxx"]
print(type(a))

#class 'tuple'#
a=(1, 2, "xxx")
print(type(a))

#class 'set'#
a={1, 2, "xxx"}
print(type(a))

#class 'dict'#
a={"a":1, "b":2}
print(type(a))

#class 'bool'#
a=True
print(type(a))

#При запросе ввода, то что вы вводите, всегда становится типом string#
x=input("Введите число: ")
y = 5 + int(x)
print(y)

x=input("Введите число: ")
y = 5 + float(x)
print(y)

x=float(input("Введите число: "))
y=float(input("Введите число: "))
r = x+y
print(r)

x=float(input("Введите число: "))
y=float(input("Введите число: "))
r = x+y
print("Результат: " + str(r))



