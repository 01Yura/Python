s1 = input()
s2 = input()

se = set(s1.split()).intersection(s2.split())
print(len(se))
