print(*[int(ch) ** 2 for ch in input().split() if int(ch) % 2 == 0 and str(int(ch) ** 2)[-1] != "4"])

