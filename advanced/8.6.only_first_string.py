se1 = set(int(el) for el in input().split())
se2 = set(int(el) for el in input().split())
print(*sorted(se1.difference(se2)))