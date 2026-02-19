num=int(input())
for i in range(1, num+1):
    for j in range(i):
        print(i, end='')
    print()


n=int(input())
x=1

for i in range(1, n+1):
  print(str(x)*i)
  x+=1