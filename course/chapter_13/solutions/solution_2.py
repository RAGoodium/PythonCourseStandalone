def filter_data(data, filter_func):
    return [item for item in data if filter_func(item)]
    
def even(a):
    return a % 2 == 0

data = [1, 2, 3, 4, 5, 6]
print(filter_data(data, even))