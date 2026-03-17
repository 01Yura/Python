li = input().split()
se = set()

for ch in li:
    ch = ch.lstrip("0")
    if ch in se:
        print("YES")
    else:
        print("NO")
        se.add(ch)
