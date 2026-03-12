n = int(input())
letters = "АБВГДЕЖЗИЙКЛМОП"

for i in range(n):
    class_name = input()
    if len(class_name) == 2 and class_name[0].isnumeric() and class_name[-1] in letters:
        print("YES")
    else:
        print("NO")
