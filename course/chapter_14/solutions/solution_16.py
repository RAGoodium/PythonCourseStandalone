def infinite_sequence():
    num = 1
    while True:
        yield num
        num += 1

gen = infinite_sequence()
for _ in range(5):
    print(next(gen))