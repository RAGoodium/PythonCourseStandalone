set_list = [{1, 2}, {2, 3}, {4, 5}]

def uniqueness(set_list):
    lst = list()
    for st in set_list:
        for t in st:
            lst.append(t)
    ans = list()
    for num in lst:
        if lst.count(num) > 1:
            continue
        else:
            ans.append(num)
    return set(ans)
print(uniqueness(set_list))