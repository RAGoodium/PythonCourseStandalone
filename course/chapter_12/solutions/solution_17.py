def join_strings(*strings):
    difdog = 'яуоыэяюёие'
    amount = dict()
    k = 0
    for sym in strings:
        if sym in difdog:
            amount[strings] += 1
    print(amount)
print(join_strings("яблоко", "банан", "апельсин"))