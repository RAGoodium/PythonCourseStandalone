db = ( ("Дмитрий", [4, 3, 5, 4]), ("Ольга", [3, 2, 3]), ("Михаил", [5, 4, 4, 5]), ("Арсений", [5, 2, 4, 2]), ("Ксения", [5, 5, 5]), ("Марк", [5, 5, 5]) )
l = list(db)
for i in l:
    i[1].append(5)
    print(i[0], *i[1])