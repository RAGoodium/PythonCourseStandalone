def transform_list(data, transform_func, condition_func):
    for i in range(len(data)):
        if condition_func(data[i]):
            data[i] = transform_func(data[i])
        else:
            continue
    return data
    
data = [10, -5, 0, 20, -7, 15]

def double(a):
    return a * 2

def positive(a):
    return a > 0

print(transform_list(data, double, positive))  
# Ожидается: [20, -5, 0, 40, -7, 30]