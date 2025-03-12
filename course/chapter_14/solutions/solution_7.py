def fibonacci(n):
    lst = [0, 1]
    [lst.append(lst[-2] + lst[-1]) for x in range(2, n)]
    return lst[:n:]
    
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]