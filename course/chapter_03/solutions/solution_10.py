n = int(input())
d = 2
while (n % d != 0):
    k = n % d
    d += 1
    if k == 1:
        continue
    elif n % k == 0:
        break
print(d)