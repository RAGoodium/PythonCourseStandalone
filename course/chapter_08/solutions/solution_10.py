names = list()
time = list()
while name := input():
    time.append(float(input()))
    names.append(name)
    
time_m = min(time)
ind_time_m = time.index(time_m)
    
print(f"Победитель: {names[ind_time_m]}")
print(f'Время: {time_m} минут')