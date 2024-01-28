num=int(input())
for i in range(1,int((num+2)/2)):
    print('*'*i)
print('*'*(i+1))
while not i==0:
    print('*'*i)
    i-=1


n=int(input())
x=int((n+1)/2)
for j in range(1, x+1):
  print('*'*j)
for k in range(x-1, 0, -1):
  print('*'*k)