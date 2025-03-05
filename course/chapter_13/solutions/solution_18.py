num = "1 2 3 4 5".split(" ")
num = list(map(int, num))
doub = list(map(lambda n: n * 2, num))
print(doub)