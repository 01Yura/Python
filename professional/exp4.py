a = "a" * 10
b = "a" * 10

print(a==b)
print(a is b)
print("-----------------------")

a = "Hello!"
b = "Hello!"
print(a==b)
print(a is b)

print("-----------------------")

for n in [1, 2, 10, 100, 1000, 10000, 100000]:
    s1 = "a" * n
    s2 = "a" * n
    print(n, s1 is s2)

print("-----------------------")
