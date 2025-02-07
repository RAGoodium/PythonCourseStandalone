dict1 = {'a': {1, 2}, 'b': {3, 4}}
dict2 = {'b': {5}, 'c': {6, 7}}

def merge_dicts(dict1, dict2):
    for check1 in dict2:
        if check1 in dict1:
            dict1[check1] = dict1[check1] | dict2[check1]
        else:
            dict1[check1] = dict2[check1]
            return dict1


print(merge_dicts(dict1, dict2))    