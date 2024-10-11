password = 'secret123'
a = input()
while a != password:
    print('Неверный пароль, попробуйте снова.')
    a = input()

print("Доступ разрешён.")