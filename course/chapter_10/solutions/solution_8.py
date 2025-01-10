t1 = input().split()
t2 = input().split()
t3 = input().split()
set1 = set(t1)
set2 = set(t2)
set3 = set(t3)
inter12 = set1 & set2
inter12_3 = inter12 & set3
inter = sorted(list(inter12_3))
print(*inter)