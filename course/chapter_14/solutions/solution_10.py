def square_numbers(n):
    for i in range(1, n + 1):
        square = i * i
        yield square
    
for i in square_numbers(4):
    print(i)