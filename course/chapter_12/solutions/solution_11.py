lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 4, 6, 8]

def intersect_lists(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    st = set1 & set2
    ans = sorted(list(st))
    return ans
print(intersect_lists(lst1, lst2))