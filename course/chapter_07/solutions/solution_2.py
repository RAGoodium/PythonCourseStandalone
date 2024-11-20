numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in numbers:
    if n % 2 == 0:
        if n == numbers[-1]:
            print(n)
        else:
            print(n, end=", ")
            
for n in numbers:
    if n % 2 != 0:
        if n == numbers[-2]:
            print(n)
        else:
            print(n, end=", ")