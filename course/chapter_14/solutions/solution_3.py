def sum_of_even_squares(lst):
    even = [x for x in lst if x % 2 == 0] 
    return sum([x * x for x in even])
    
print(sum_of_even_squares([1, 2, 3, 4, 5, 6]))  # 56 (2^2 + 4^2 + 6^2)