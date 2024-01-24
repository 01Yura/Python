n = int(input())
for i in range(2, n):
    if n % i == 0:
        break
print(i)


n = int(input())
delit = 2
while delit > 1:
    if n % delit == 0:
        break
    else:
        delit += 1
print(delit)
