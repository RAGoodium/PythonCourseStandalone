str = input()
alp = list()
for sym in str:
    if sym == " ":
        continue
    else:
        alp.append(sym)
uni = set(alp)
alp = sorted(list(uni))

print('Уникальные символы:', *alp)