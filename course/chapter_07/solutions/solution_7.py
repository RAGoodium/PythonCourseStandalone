numbers = [5, 10, 15, 20, 25, 30, 35, 40]
amount = len(numbers)
sum = 0

for n in range(amount):
    sum = sum + int(numbers[n])
print(f'Среднее арифметическое: {sum / amount}')