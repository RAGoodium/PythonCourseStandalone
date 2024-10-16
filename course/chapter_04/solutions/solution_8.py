n = int(input())

n1 = 1 # 1 2 5 13 
n2 = 1 # 1 3 8 21

print('Числа Фибоначчи:')
for i in range(n // 2):
    print(n1)
    print(n2)

    n1 = n1 + n2
    n2 = n1 + n2
