def reverse_strings(lst):
    return ([x[::-1] for x in lst])
print(reverse_strings(["hello", "world"]))  # ['olleh', 'dlrow']