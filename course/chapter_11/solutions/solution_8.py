author = dict()
while name_book := input():
    name, book = name_book.split(": ")
    if name not in author:
        author[name] = [book]
    else:
        author[name].append(book)
for oc in author:
    print(oc, ': ', ", ".join(author[oc]), sep="")