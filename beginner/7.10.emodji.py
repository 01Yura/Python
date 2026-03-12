n = int(input())
m = int(input())
flag = False

for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            if i + 3 * j + 2 * k == m:
                print(str(i) + " + 3×" + str(j) + " + 2×" + str(k) + " = " + str(m))
                flag = True
if not flag:
    print("При заданных n и m решений не существует.")