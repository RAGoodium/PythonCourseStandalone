def greet_users(*names):
    s = ""
    for name in names:
        hi = f'Привет, {name}!\n'
        s = s + hi
    return s
print(greet_users("Анна", "Иван", "Мария"))