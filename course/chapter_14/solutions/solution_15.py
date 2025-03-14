def multiples_of_3_or_5(n):
    for num in range(1, n + 1):
        if (num % 3 == 0 or num % 5 == 0):
            yield num

for i in multiples_of_3_or_5(15):
    print(i)