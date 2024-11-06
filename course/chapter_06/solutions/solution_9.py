w = int(input())
h = int(input())
t = 0

k = h * w
max_len = len(str(k))

for u in range (1, h):
    for i in range(w + 1):
        num = u + i * h - i
        num_len = len(str(num)) - 1
        s = " " * (max_len - num_len)
        
        if num == k - i + u: 
            print(num, end="", sep="")
        else:
            print(num, s, end="", sep="")
    print()
    