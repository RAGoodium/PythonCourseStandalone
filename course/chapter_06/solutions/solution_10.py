n = 5 #int(input())

for i in range(1, n + 1):
    for k in range(1, n + 2):

        if k > i:
            print(i, '\t', end="", sep="")
        elif k < i:
            print(k, '\t', end="", sep="")
            

    print()
