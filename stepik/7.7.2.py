mx = -1*(10**6)
s = 0
count=0
for i in range(10):
    x = int(input())
    if x < 0:
        s = s + x
        count+=1
        if x > mx:
            mx = x
if count==0:
  print('NO')
else:
  print(s)
  print(mx)