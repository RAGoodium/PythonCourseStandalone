def swap_keys_values(d):
    revers = dict()
    for key, value in d.items():
        if key not in revers:
            revers[value] = key
        else:
            revers[value] += key
    return revers

d = {'a': 1, 'b': 2, 'c': 3}
print(swap_keys_values(d))