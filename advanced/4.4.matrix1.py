rows = int(input())
cols = int(input())
matrix = list()

for i in range(rows):
    matrix.append([input() for _ in range(cols)])

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()
