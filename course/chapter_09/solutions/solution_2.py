s = input()
s = s.lower()
amount = 0
for n in s:
    if n in "аеёиоуэюя":
        amount += 1
print(f'Количество гласных букв: {amount}')