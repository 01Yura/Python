num = input()
if len(num) == 5:
    num_list = list(num)
    num_list.reverse()
    print(int("".join(num_list)))
else:
    first = num[0]
    num_list = list(num[1:])
    num_list.reverse()
    print(first + "".join(num_list))
