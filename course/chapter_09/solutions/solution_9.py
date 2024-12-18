n = input()
s = ""
for i in n:
    if i.isnumeric():
        continue
    else:
        s += i
print(s)