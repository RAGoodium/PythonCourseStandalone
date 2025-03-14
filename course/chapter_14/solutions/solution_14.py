def fibonacci(n): #HEEEEEEEEELL NAH
    a = 1
    b = 1
    for t in range(n):
        if t < 2:
            yield 1
        else:
            a,b = b, b + a
            yield b

        
for i in fibonacci(7):
    print(i)                # 0, 1, 1, 2, 3, 5, 8