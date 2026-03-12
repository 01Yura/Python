# Обратите внимание: при 0 < n < m результатом деления n % m является число n, а результатом деления n // m -> 0
print(8 % 90)  # result == само число 8
print(10 // 12)  # 10 / 12 = 0.833333...
print()

print(10 // 3)
print(-10 // 3)

print(4 / 2)
print(9 % 10)
print()
print(0 % 2)
print(1 % 2)
print()

num = 1234567
last_2_digit = num % 100
print(last_2_digit)

print()

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)