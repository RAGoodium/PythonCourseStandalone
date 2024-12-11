db = ( ("Дмитрий", [4, 3, 5, 4]), ("Ольга", [3, 2, 3]), ("Михаил", [5, 4, 4, 5]), ("Арсений", [5, 2, 4, 2]), ("Ксения", [5, 5, 5]), ("Марк", [5, 5, 5]) )
bad = list()
for i in db:
    f = i[1].count(2)
    bad.append(f)
    bad_max = max(bad)
    bad_max_ind = bad.index(bad_max)
print(db[bad_max_ind][0])