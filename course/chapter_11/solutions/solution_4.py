n = input()
symbols = dict()
q = None
for sym in n:
    if sym in symbols:
        symbols[sym] += 1
    else:
        symbols[sym] = 1

for key, val in symbols.items():
    if val == 1:
        print(key)
        break
else:
    print(q)