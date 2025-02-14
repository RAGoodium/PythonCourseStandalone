def join_strings(*strings):
    difdog = 'аяуоыэяюёие'
    amount = dict()
    k = 0
    l = list()
    # for word in strings:
    #     l.append(word)
    # for word in l:
    #     if word not in amount:
    #         amount[word] = 0
    #     for sym in word:
    #         if sym in difdog:
    #             amount[word] += 1
    # print(amount)
    
    for word in strings:
        for sym in word:
            if sym in difdog:
                k += 1
        if k not in amount:
            amount[k] = [word]
        else:
            amount[k].append(word)
        k = 0
        nums = list()
        for num in amount:
            nums.append(num)
    answ = sorted(amount[max(nums)])
    print(answ)
    if len(answ) == 1:
        for m in answ:
            return m
    else:
        return answ

#print(join_strings("яблоко", "банан", "апельсин"))
print(join_strings("кушать", "пить"))
