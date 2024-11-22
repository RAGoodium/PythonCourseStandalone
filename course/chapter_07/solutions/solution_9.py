l = list()
while num := input():
    l.append(int(num))

l.sort()
print(f'Минимальная оценка: {l[0]}')
print(f'Максимальная оценка: {l[-1]}')
print(f'Отсортированные оценки: {l}')
