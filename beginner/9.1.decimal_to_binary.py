num = int(input())
decimal_string = ""

while num != 0:
    if num % 2 == 0:
        decimal_string += "0"
        num //= 2
    else:
        decimal_string += "1"
        num //= 2

result = ""
for i in range(1, len(decimal_string) + 1):
    result += decimal_string[-i]

print(result)
