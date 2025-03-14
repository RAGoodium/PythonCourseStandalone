def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count +=1

for i in count_up_to(5):
    print(i)