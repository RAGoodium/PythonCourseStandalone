n = 5 #int(input())

for i in range(n, 0, -1):
    d = n - i
    for k in range(n, d, -1):
        print(k, end="")
    print()