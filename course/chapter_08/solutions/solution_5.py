matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for n in matrix:
    for i in n:
        if i == 7 or i == 8 or i == 9:
            print(i, end="")
        else:
            print(i, end=" ")
    print()