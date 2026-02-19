a,b=int(input()), int(input())
counter=0
for i in range(a,b+1):
    if i**3%10==4 or i**3%10==9:
        counter+=1
print(counter)



tot = 0
for i in range(int(input()), int(input()) + 1):
    if str(i ** 3 % 10) in '49':
        tot += 1
print(tot)