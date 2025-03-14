def my_range(a, b):
    while a != b:
        yield a
        a += 1


for i in my_range(4, 8):
    print(i)