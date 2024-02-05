n = int(input())
for i in range(1, n + 1):
    count = 0
    for divisor in range(1, i + 1):
        if i % divisor == 0:
            count += 1
    print(i, '+'*count, sep='')


n=int(input())
for i in range(1, n+1):
  delit=0
  sum=0
  print(i, end='')
  for delit in range(1, i+1):
    if i%delit==0:
      sum+=1
  print('+'*sum, sep='', end='')
  print()