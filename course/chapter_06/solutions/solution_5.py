n = int(input())
for d in range(1, n + 1):
    k = 0
    for i in range(1, d + 1):
        if d % i == 0:
            k += 1
    if k == 2:
        print(d)
        