lst = ['apple', 'banana', 'kiwi', 'grape']

#список длин слов и отсортировать его
#словарь 'длина: пустой список'
#добавить значения слов по сравнивая ключи и длину слов
l = list()
for w in lst:
    l.append(len(w))
l = sorted(l)

for w range(l)