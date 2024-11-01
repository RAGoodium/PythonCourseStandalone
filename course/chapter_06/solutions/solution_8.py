t = int(input())
s = 0
while t > 0:
    n = int(input())
    while n > 0:
        d = n % 10
        s += d
        n = n // 10
    t -= 1 
print(s)