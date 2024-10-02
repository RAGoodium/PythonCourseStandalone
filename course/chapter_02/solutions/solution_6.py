t = int(input())

if t >= 6 and t <= 11:
    print('Доброе утро!')
elif t >= 12 and t <= 17:
    print('Доброй день!')
elif t >= 18 and t <= 21:
    print('Доброй вечер!')
elif t >= 22 and t <= 24 or t >= 0 and t <= 5:
    print('Доброй ночи!')