


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "На ноль делить нельзя"
    
def create_operation(op): #op = "add"
    if op == "add":
        return add
    elif op == "subtract":
        return subtract
    elif op == "multiply":
        return multiply
    elif op == "divide":
        return divide
    
#operation = input()   
#my_func = create_operation()
#print(my_func(4, 6)) # Ожидается: 10
