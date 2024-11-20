numbers = [12, -7, 5, -3, 8, -2]

for n in range(len(numbers)):
    if 0 > numbers[n]:
        numbers[n] = 0
print(f'Список после замены: {numbers}')