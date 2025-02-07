lst = ['apple', 'banana', 'kiwi', 'grape']

#список длин слов и отсортировать его
#словарь 'длина: пустой список'
#добавить значения слов по сравнивая ключи и длину слов
def sort_by_length(lst):
    l = list()
    for lon in lst:
        l.append(len(lon))
    l = sorted(l)

    d = dict()
    for num in l:
        if num not in d:
            d[num] = []
        else:
            continue

    for w in lst:
        ln = len(w)
        if ln not in d:
            d[ln] = [w]
        else:
            d[ln].append(w)

    done = list()
    for srtd in d.values():
        for words in srtd:
            done.append(words)
    return done
