n = 0 #-3 1     3       -100 101        -1 -2 6235
s = 0
while n < 1:
    
    n = int(input())

while n > 0:
    d = n % 10
    s += d
    n = n // 10
print(s)