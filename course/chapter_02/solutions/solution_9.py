nu1 = int(input()) #12 32 10 50
nu2 = int(input()) #70 50 50 20

if (
    (
    (20 >= nu1 >= 10)
    or #1 из них True
    (60 >= nu1 >= 50)
    ) 
    and #Оба либо True = диапазон, либо False = вне
    (
    (20 >= nu2 >= 10)
    or #1 из них True
    (60 >= nu2 >= 50)
    )
    ):
    print("Числа в диапазоне.")
else:
    print("Числа вне диапазона.")