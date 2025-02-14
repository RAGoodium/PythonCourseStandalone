def generate_report(name, *args, **kwargs):
    answ = (f'Отчёт для {name}')
    rg = list()
    for arg in args:
        rg.append(arg)
    answ = answ + '\n'
    r = ('Выполненные задачи: ')
    g = ", ".join(rg)
    arg = r + g
    answ += arg
    for key, value in kwargs.items():
        answ = answ + '\n'
        answ = answ + (f'{key}: {value}')

    return answ    
generate_report("Анна", "Задача1", "Задача2", "Задача3", productivity=85, overtime=10)
# Ожидается:
# Отчёт для Анна
# Выполненные задачи: Задача1, Задача2, Задача3
# productivity: 85
# overtime: 10
