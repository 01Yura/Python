num = int(input())
flag = 'YES'
last_digit = num % 10
while num != 0:
    penultimate_digit = last_digit
    last_digit = num % 10
    if penultimate_digit == last_digit:
        num //= 10
    else:
        flag = 'NO'
print(flag)


n=int(input())
y=0
if len(str(n))==1:
  y='YES'
else:
  while y!='NO' and n!=0:
    x=n%10
    v=x
    n=n//10
    if n>=2:
      z=n%10
    if v==z:
      y='YES'
    else:
      y='NO'
print(y)