# не дорешал

rows = int(input())
columns = int(input())
matrix = list()

for _ in range(rows):
    matrix.append([input() for _ in range(columns)])

for row in matrix:
    for el in row:
        print(el, end=" ")
    print()

print()

for i in range(rows):
    for j in range(columns):
        print(matrix[j][i], end=" ")
    print()
