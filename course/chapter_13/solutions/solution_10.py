def apply_functions_sequence(data, func_list):
    for i in range(len(data)):
        for func in func_list:
            data[i] = func(data[i])
    return data

data = [1, 2, 3]

def increment(a):
    return a + 1

def doubler(a):
    return a * 2

func_list = [increment, doubler]

print(apply_functions_sequence(data, func_list))  
# Ожидается: [4, 6, 8]