numbers = [4, 7, 2, 9, 8, 5, 6, 3, 0, 1]
a = list()
for n in range(len(numbers)):
    if numbers[n] % 2 == 0:
        a.append(n)
for nu in range(len(a)):
    if a[nu] == a[-1]:
        print(a[nu])
    else:
        print(a[nu], end=', ')