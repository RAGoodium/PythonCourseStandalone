year = int(input())
month = int(input())
day = int(input())
date1 = (year, month, day)

year = int(input())
month = int(input())
day = int(input())
date2 = (year, month, day)

if date1 > date2:
    print(f'{date1} > {date2}')
elif date1 < date2:
    print(f'{date1} < {date2}')
elif date1 == date2:
    print(f'{date1} = {date2}')