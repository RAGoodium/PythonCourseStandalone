for a in range(1, 501): 
    for b in range(a, 501):
        c = 1000 - (a + b)
        if a*a + b*b == c*c:
            print(a, b, c)
