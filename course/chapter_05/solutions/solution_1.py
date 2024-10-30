n = int(input())


for i in range(1, n + 1):
    for u in range(1, n + 1): 
        print(u * i, '\t', end="", sep="")
    print()
