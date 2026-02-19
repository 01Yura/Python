m, p, n = float(input()), int(input()), int(input())
x=m
print('1', m)
for i in range(n-1):
  x=(x+(x/100*p))
  print(i+2, x)



m, p, n = int(input()), int(input()), int(input())
cur_population = float(m)

for i in range(n):
    print(i + 1, cur_population)
    cur_population = cur_population * (1 + p / 100)