str1 = input() #abcde
str2 = input() #ncdefg
alp1 = list()
alp2 = list()
for sym in str1:
    if sym == " ":
        continue
    else:
        alp1.append(sym)
for sym in str2:
    if sym == " ":
        continue
    else:
        alp2.append(sym)
uni1 = set(alp1)
uni2 = set(alp2)
inter = uni1.intersection(uni2)
inter_sort = sorted(list(inter))
print(*inter_sort)