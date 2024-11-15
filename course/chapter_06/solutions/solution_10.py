n = int(input())

for i in range(n + 1):
    for k in range(n + 1):

        sl = min(n - i, n - k, i, k) + 1
        
        if i == n // 2:
            continue
        else:
         
            if k > i:
                if k == n:
                    print(sl, end="\n", sep="")
                else:
                    print(sl, end=" ", sep="")
            elif k < i:
                if k == n - 1:
                    print(sl, end="\n", sep="")
                else:
                    print(sl, end=" ", sep="")

