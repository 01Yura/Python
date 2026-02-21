x = int(input())

if 999 < x < 10000 and (x % 17 == 0 or x % 7 == 0):
    print("YES")
else:
    print("NO")