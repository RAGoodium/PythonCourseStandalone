age = int(input())
invite = str(input())

if invite == 'Y':
    invite == True
elif invite == 'N':
    invite == False
else:
    print('Введите корректные значения.')

if age >= 18 and invite:
    print('Добро пожаловать в клуб!')
else:
    print('Извините, вход запрещен..')