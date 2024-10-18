n = int(input()) #1 3 101 6235
s = 0

while n > 0:
    d = n % 10
    s += d
    n = n // 10
print(s)