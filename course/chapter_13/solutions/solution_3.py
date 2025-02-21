def apply_multiple(data, func1, func2):
    return [func2(func1(item)) for item in data]


def increment(a):
    return a + 1

def sqr(a):
    return a * a

data = [1, 2, 3, 4]
print(apply_multiple(data, increment, sqr))