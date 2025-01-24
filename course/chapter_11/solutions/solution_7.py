inp = input().split()
idk = []
for s in inp:
    if s in idk:
        a = str(inp.count(s))
        sym = (s + "_" + a)
        idk.append(sym)
    else:
        idk.append(s)
print(*idk)