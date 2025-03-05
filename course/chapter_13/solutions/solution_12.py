num = input().split(" ")
num = list(map(int, num))
squares = list(map(lambda x: x * x, num))
print(squares)  # [1, 4, 9, 16] 