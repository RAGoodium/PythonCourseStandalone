inp = input().split()
d = dict()
l = list()
for s in inp:
    if s in d:
        d[s] += 1
        n = (s + "_" + str(d[s]))
        l.append(n)
    else:
        d[s] = 0
        l.append(s)

print(" ".join(l))