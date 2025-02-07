matrix = [[1, 2, 3], [1, 2, 1], [3, 1, 2]]

def replace_in_matrix(matrix, old_value, new_value):
    new_matrix = matrix.copy()
    matrix.clear()
    for lst in new_matrix:
        l = list()
        for num in lst:
            if num == old_value:
                l.append(new_value)
            else:
                l.append(num)

        matrix.append(l)
    
    
            
print(replace_in_matrix(matrix, 1, 9))