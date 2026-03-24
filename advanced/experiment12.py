fruits = "apple banana apple orange banana apple"
fruits = fruits.split()
di = {}
for fruit in fruits:
    di[fruit] = di.setdefault(fruit, 0) + 1
print(di)