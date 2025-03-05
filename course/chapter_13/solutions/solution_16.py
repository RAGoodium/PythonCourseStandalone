l1 = "2 3 4".split(" ")
l2 = "3 2 1".split(" ")
l1 = list(map(int, l1)) #[2, 3, 4]
l2 = list(map(int, l2)) #[3, 2, 1]
omni = lambda x1, x2: x1 ** x2
o1 = omni(l1[0], l2[0])
o2 = omni(l1[1], l2[1])
o3 = omni(l1[2], l2[2])
l = [o1, o2, o3]
print(l)       

