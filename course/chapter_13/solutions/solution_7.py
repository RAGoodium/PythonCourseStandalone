def apply_to_matrix(matrix, func):
    new_matrix = list()
    for duo in matrix:
        new_duo = list()
        for num in duo:
            numb = func(num)
            new_duo.append(numb)
        new_matrix.append(new_duo)
    return new_matrix
    
matrix = [[1, 2], [3, 4]]

def double(a):
    return a * 2

print(apply_to_matrix(matrix, double))  
# Ожидается: [[2, 4], [6, 8]]