matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for x in range(3):
    for y in range(3):
        if matrix[y][x] in [7, 8, 9]:
            print(matrix[y][x], end='')
        else:
            print(matrix[y][x], end=' ')
    print()