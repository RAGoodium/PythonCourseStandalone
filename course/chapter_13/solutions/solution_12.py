num = input()
for n in num:
    num[n] = lambda n: n * n
print(num)