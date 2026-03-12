num = int(input())
x = (num+1 )// 2

for i in range(1, x+1):
    print("*" * i, end="")
    print()

for i in range(x - 1, 0, -1):
    print("*" * i, end="")
    print()
