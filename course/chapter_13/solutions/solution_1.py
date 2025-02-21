def apply_to_all(data, func):
    return [func(item) for item in data]
def sqr(a):
    return a * a

data = [1, 2, 3, 4, 5]
print(apply_to_all(data, sqr)) 