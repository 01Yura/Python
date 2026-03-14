list1 = [[7, 15], [2, 3, 5, 10], [4]]

maximum = list1[0][0]
for li in list1:
    current_max = max(li)
    if current_max > maximum:
        maximum = current_max

print(maximum)