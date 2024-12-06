books = list()
pages = list()
while name := input():
    pages.append(int(input()))
    books.append(name)
    
pag_m = max(pages)
ind_pag_m = pages.index(pag_m)
    
print(f"Самая толстая книга: ('{books[ind_pag_m]}', {pag_m})")
print(f'Суммарное число страниц: {sum(pages)}')