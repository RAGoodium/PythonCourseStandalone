l = list()
while name := input():
    l.append(name)
    
while name := input():
    l.append(name)

while name := input():
    if name not in l:
        print('такой игрушки нет')
    else:
        l.remove(name)
    
print(l)