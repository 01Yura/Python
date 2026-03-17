num1_set = set(input())
num2_list = list(input())

if num1_set.issuperset(num2_list):
    print("YES")
else:
    print("NO")
