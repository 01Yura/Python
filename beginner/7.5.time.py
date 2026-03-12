h1, m1, h2, m2 = int(input()), int(input()), int(input()), int(input())
time1 = h1 * 60 + m1
time2 = h2 * 60 + m2

for i in range(time1, time2 + 1):
    h = str(i // 60)
    m = str(i % 60)

    if len(h) == 1:
        h = "0" + h
    if len(m) == 1:
        m = "0" + m

    print(h + ":" + m)
