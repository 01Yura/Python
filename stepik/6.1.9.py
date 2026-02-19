a, b, c = int(input()), int(input()), int(input())
max_num=max(a,b,c)
min_num=min(a,b,c)
middle_num=((a+b+c)-max_num-min_num)
print(max_num, middle_num, min_num, sep='\n')



a=int(input())
b=int(input())
c=int(input())
x=max(a, b, c)
y=min(a, b, c)
z=(a+b+c-x-y)
print(x, z, y, sep='\n')