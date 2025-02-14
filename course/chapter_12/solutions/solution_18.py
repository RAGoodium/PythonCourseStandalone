def user_info (name, **kwargs):
    answ = (f'Имя: {name}')
    for key, value in kwargs.items():
        answ = answ + '\n'
        data = f"{key}: {value}"
        answ = answ + data
    return answ
print(user_info("Анна", age=25, city="Москва", job="Программист"))