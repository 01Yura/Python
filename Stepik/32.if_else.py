num = int(input())
digit1 = num // 1000
digit2 = (num // 100) % 10
digit3 = (num // 10) % 10
digit4 = num % 10
if digit1 + digit4 == digit2 - digit3:
    print("ДА")
else:
    print("НЕТ")


num = int(input())
a = num // 1000
b = (num % 1000) // 100
c = (num % 100) // 10
d = num % 10
if a + d == b - c:
    print("ДА")
else:
    print("НЕТ")
