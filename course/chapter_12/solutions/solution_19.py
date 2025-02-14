def multiply_all(*numbers):
    l = list()
    answ = 1
    for num in numbers:
        answ = answ * num
    return answ

print(multiply_all(2, 3, 4))