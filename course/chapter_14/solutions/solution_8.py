def flatten(matrix):
    flattened = [num for row in matrix for num in row]
    return flattened

matrix = [[1, 2], [3, 4], [5, 6]]
print(flatten(matrix))  # [1, 2, 3, 4, 5, 6]