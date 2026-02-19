from math import factorial

n=int(input())
sum=0
for i in range(1, n+1):
  f=factorial(i)
  sum+=f
print(sum)