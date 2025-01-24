own_cat = dict()
while mail_name := input():
    cat, age, f_name, s_name = mail_name.split()
    owner = f_name + ' ' + s_name
    l = (cat + ', ' + age)
    if owner not in own_cat:
        own_cat[owner] = [l]
    else:
        own_cat[owner].append(l)
for oc in own_cat:
    print(oc, ': ', "; ".join(own_cat[oc]), sep="")