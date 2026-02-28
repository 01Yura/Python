n = int(input())
print(
    n // (10 ** (len(str(n)) - 2)) % 10
)
