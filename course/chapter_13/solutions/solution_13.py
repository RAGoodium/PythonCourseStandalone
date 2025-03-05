num = "1 2 3 4 5 6 7 8".split(" ")
#num = input().split(" ")
num = list(map(int, num))
even_numbers = list(filter(lambda x: x % 2 == 0, num))
print(even_numbers)

#[2, 4, 6, 8]