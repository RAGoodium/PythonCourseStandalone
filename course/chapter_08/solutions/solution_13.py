db = ( ("Дмитрий", [4, 3, 5, 4]), ("Ольга", [3, 2, 3]), ("Михаил", [5, 4, 4, 5]), ("Арсений", [5, 2, 4, 2]), ("Ксения", [5, 5, 5]), ("Марк", [5, 5, 5]) )
name = input()

flag = False
for k in db:
    if k[0] == name:
        print(*k[1])
        flag = True
        break
if flag == False:
    print('такого ученика нет')