n = input().split()
answ = list()
for word in n:
    if word.isalpha() == True:
        answ.append(word.title())
    else:
        answ.append(word)
        
                            #привет мир это python3
print('Результат:', " ".join(answ)) #Результат: Привет Мир Это python3