def even_numbers(lst):
    even = [x for x in lst if x % 2 == 0]
    return even
print(even_numbers([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]