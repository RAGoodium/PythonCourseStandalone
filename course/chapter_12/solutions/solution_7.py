def count_unique_elements(lst):
    word_count = dict()
    for word in lst:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
lst = [1, 2, 3, (1, 2), 3, 2, 1, (1, 2), 1]
print(count_unique_elements(lst))