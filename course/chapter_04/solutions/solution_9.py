n1 = int(input())
n2 = int(input())
n = int(input())

for i in range(n // 2):
    print(n1)
    print(n2)

    n1 = n1 + n2
    n2 = n1 + n2