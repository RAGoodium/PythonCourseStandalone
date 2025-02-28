def apply_to_nested_list(nested_list, func):
    for lst in range(len(nested_list)):
        if isinstance(nested_list[lst], list):
            apply_to_nested_list(nested_list[lst], func)
        else:
            nested_list[lst] = func(nested_list[lst])
    return nested_list

nested_list = [[1, 2, 3], [4, [4, 5]], [6, 7, 8, 9]]

def sqr(a):
    return a * a

print(apply_to_nested_list(nested_list, sqr))  
# Ожидается: [[1, 4, 9], [16, [16, 25]], [36, 49, 64, 81]]