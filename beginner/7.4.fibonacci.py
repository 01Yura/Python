n = int(input())

prev = 1
pred_prev = 0

if n == 1:
    print(1)
else:
    print(1, end=" ")
    for i in range(2, n + 1):
        current = pred_prev + prev
        pred_prev = prev
        prev = current
        if i < n:
            print(current, end=" ")
        else:
            print(current)


# ----------------------------------------

n = int(input())
a, b = 1, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b

# ----------------------------------------


prev_prev = 1
prev = 1

for i in range(n):
    print(prev_prev, end=' ')
    current = prev_prev + prev
    prev_prev = prev
    prev = current