st = "apple banana avocado cherry apricot".split(" ")
srt = list(sorted(st, key=lambda x: x[1]))
print(srt[2::])