def sum_bin_num(n, one):
    #Посчитать количество 1 в двочиной, без bin 
    res = 0
    one = 1
    n = 127
    while one < n:
        if (one & n):
            res += 1
        one = one << 1 
    return res
print(sum_bin_num(127, 1))

def kruti_muti(n):
    #Число в двоичном, 2 функции (1 - крайний правый в начало, 2 - первый в конец)
    n = bin(n)
    strt = n[0:1:]
    end = n[:-1:-1]
    
    
print(kruti_muti(8)) #1000 | 0001 | 0100

n = bin(8)
strt = n[0:1:]
end = n[:-1:-1]
print()