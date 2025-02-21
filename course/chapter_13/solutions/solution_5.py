def find_max_by(data, key_func):
    l = [key_func(item) for item in data]
    mx = max(l)
    return data[l.index(mx)]

def abs_value(a):
    return abs(a)

data = [-10, -20, 5, 3]
print(find_max_by(data, abs_value))