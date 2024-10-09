age = int(input())      # 21 21 -14
invite = str(input())   # Y  N  q

if (invite == "Y"
    or
    invite == "N"
    and
    age >= 0
    ):
    if age >= 18 and invite == "Y":
       print('Добро пожаловать в клуб!')
    else:
        print('Извините, вход запрещен.')
else:
    print('Введите корректные значения.')
