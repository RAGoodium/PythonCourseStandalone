numbers = [3, 17, 6, 12, 9, 21, 5]
a = 0
for n in numbers:
    if n > a:
        a = n
    else:
        continue
print(f'Максимальный элемент: {a}')