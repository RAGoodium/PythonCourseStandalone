timer = 0
s = 0
while timer != 5:
    n = int(input())
    if n > 0:
        s = s + n
        timer += 1
    else:
        continue
print(s)