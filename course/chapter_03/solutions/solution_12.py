num = 12
tries = 5
n = 0
while tries > 0 and n != num:
    tries -= 1
    n = int(input())
    if n > num:
        print('Загаданное число меньше.')
    elif n < num:
        print('Загаданное число больше.')
if n == num:
    print('Поздравляем! Вы угадали число.')
if tries == 0:
    print("Попытки закончились")