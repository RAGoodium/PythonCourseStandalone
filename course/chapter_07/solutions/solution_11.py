l = list()
while things := input():
    l.append(things)

if 'Палатка' not in l:
    print('Вы не взяли палатку!')

print(len(l))