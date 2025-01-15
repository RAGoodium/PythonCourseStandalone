students = dict()
while name_grade := input():
    name, grade = name_grade.split(": ")
    grade = int(grade.strip())
    if grade not in students:
        students[grade] = [name]
    else:
        students[grade].append(name)
for keys in students:
    name = students[keys]
    print(f'Класс {keys}: {", ".join(name)}')