items = input().split(" ")
#lens = list(map(len, items))
print(sorted(items, key=lambda x: len(x)))