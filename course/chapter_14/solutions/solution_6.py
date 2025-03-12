def multiples_of_3_and_5(n):
    return ([x for x in range(n) if (x % 3 == 0 and x % 5 == 0)])

print(multiples_of_3_and_5(50))  # [0, 15, 30, 45]