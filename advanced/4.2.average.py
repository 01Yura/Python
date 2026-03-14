list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

summary = 0
counter = 0

for li in list1:
    for el in li:
        summary += el
        counter += 1

print(summary / counter)
