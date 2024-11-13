n = 5 #int(input())

for i in range(n + 1):
    for k in range(n + 1):

        sl = min(i, k, n - i, n - k) + 1
                 
        if k > i:
            if k == n:
                print(sl, end="", sep="")
            else:
                print(sl, end=" ", sep="")
        elif k < i:
            if k == n - 1:
                print(sl, end="", sep="")
            else:
                print(sl, end=" ", sep="")
    print()
