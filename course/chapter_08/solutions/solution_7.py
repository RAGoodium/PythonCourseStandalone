x = float(input())
y = float(input())
coord = (x,y)
start = (10.5, 22.7)

if coord == start:
    print('Вы находитесь в начальной точке маршрута')
else:
    print(round(start[0] - x, 1))
    print(round(start[1] - y, 1))