a = int(input()) # 4 4 14 4
b = int(input()) # 5 15 5 5
c = int(input()) # 6 3 6 16

if ((c <= a + b) and
    (a <= c + b) and
    (b <= c + a)):
    print('Такой треугольник существует')
else:
    print('Такой треугольник не существует')