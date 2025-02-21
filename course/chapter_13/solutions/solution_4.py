def check_all(data, check_func):
    if [item for item in data if check_func(item) == False]:
        return False
    else:
        return True
        
def positive(a):
    return a > 0

data = [1, 2, 3, 4, 0]
print(check_all(data, positive))