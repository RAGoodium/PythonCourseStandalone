def factorials(n):
    fac = 1
    for num in range(2, n + 2):
        yield fac
        fac = fac * num
for i in factorials(5):
    print(i)