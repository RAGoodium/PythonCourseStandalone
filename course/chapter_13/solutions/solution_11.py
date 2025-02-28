def multi_criteria_sort(data, func1, func2):
    sorted_pairs = sorted(data, key=func1)
    sorted_pairs = sorted(data, key=func2)
    return sorted_pairs
data = [(1, 5), (2, 3), (1, 2), (2, 7), (1, 4)]

print(multi_criteria_sort(data, lambda x: x[0], lambda x: x[1]))  
# Ожидается: [(1, 2), (1, 4), (1, 5), (2, 3), (2, 7)]