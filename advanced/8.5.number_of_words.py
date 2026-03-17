string = input()
processed_str = string.lower()

for ch in ".,:;-!?":
    processed_str = processed_str.replace(ch, "")

processed_str = " ".join(processed_str.split())

li = processed_str.split()

se = set(li)

print(len(se))
