a=input()
b=input()
c=input()
x=len(a)
y=len(b)
z=len(c)
max1=max(x, y, z)
min1=min(x, y, z)
if min1==x:
    small=a
elif min1==y:
    small=b
else:
    small=c
if max1==x:
    big=a
elif max1==y:
    big=b
else:
    big=c
print(small, big, sep='\n')