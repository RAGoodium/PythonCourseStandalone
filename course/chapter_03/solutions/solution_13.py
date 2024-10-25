password = 'pass'
tries = 3
s = ""
while tries > 0 and s != password:
    
    s = input()
    
    tries -= 1
    
    if tries > 0:
        
        if s != password:
            print("Неверный пароль, попробуйте снова.")

if s == password:
    print('Доступ разрешён.')
    tries += 1000
    
if tries == 0:
    print("Доступ запрещен")