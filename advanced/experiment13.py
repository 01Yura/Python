fruits = "apple banana apple orange banana apple"
di = {el: len(el) for el in fruits.split()}
print(di)

print(type(1))
numbers = [1, 2, "1", "2", -4, 3, 4]
s = {el for el in numbers if type(el) == int}
print(s)
