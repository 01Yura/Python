n = int(input())
total = n
while total >= 10:
    n = int(total)
    total=0
    while not n <= 0:
        x = n % 10
        n = n - x
        total += x
        n = n / 10
        
print(int(total))

n=int(input())
a=n
while len(str(a))!=1:
  n=a
  sum=0
  while n>0:
    x=n%10
    n=n//10
    sum=sum+x
    a=sum
print(a)