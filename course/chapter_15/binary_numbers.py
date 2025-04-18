def sum_bin_num(n, one):
    #Посчитать количество 1 в двочиной, без bin 
    res = 0
    one = 1
    n = 127
    while one < n:
        if (one & n):
            res += 1
        one = one << 1 
    return bin(n), res
print(sum_bin_num(127, 1))

def kruti_muti(n):
    #Число в двоичном, 2 функции (1 - крайний правый в начало, 2 - первый в конец)
    one = 1
    n1, n2 = n, n
    while one < n1:
        one <<= 1
    if 1 & n1:
        n1 += one 
    n1 >>= 1 

    while one < n2:
        one <<= 1
    n2 <<= 1
    n2 ^= one 
    n2 += 1 
    return bin(n), bin(n1), bin(n2)
print(kruti_muti(21)) #1000 | 0001 | 0100

#def mask()
