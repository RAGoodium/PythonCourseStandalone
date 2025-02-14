def find_max(a, b, *args):
    l = list()
    l.append(a) 
    l.append(b)
    for num in args:
        l.append(num)
    return max(l)
print(find_max(2, 5, 9, 3))