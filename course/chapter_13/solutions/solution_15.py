nums = "1 3 4 1 5 2 2 5".split(" ")
list = list(map(int, nums))
l1 = list[0::2]
l2 = list[1::2]
pairs = zip(l1, l2)
s_pairs = sorted(pairs, key=lambda x: x[1])

print(s_pairs)