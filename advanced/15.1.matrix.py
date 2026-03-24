def matrix(row=None, col=None, value=0):
    if row == None and col == None:
        col, row = 1, 1
    if row >=1 and col == None:
        col = row
    m = []
    for i in range(row):
        li = []
        for j in range(col):
            li.append(value)
        m.append(li)
    return m


print(matrix())
print(matrix(3))
print(matrix(3,4,9))
print(matrix(3, 1))
