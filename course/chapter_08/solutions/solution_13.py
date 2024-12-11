db = ( ("Дмитрий", [4, 3, 5, 4]), ("Ольга", [3, 2, 3]), ("Михаил", [5, 4, 4, 5]), ("Арсений", [5, 2, 4, 2]), ("Ксения", [5, 5, 5]), ("Марк", [5, 5, 5]) )
name = str(input())
for i in db:
    if name in i:
        y = 1
    elif name not in i:
        y = 0
    name_ind = i.index(name)
    if y == 1:
        print(*db[name_ind][1])
    else:
        print("такого ученика нет")