n=int(input())
largest1=0
largest2=0
for i in range(n):
  x=int(input())
  if largest1<x:
    largest2=largest1
    largest1=x
  if largest1>x and largest2<x:
      largest2=x
print(largest1, largest2, sep='\n')