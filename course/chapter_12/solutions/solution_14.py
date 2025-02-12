word_list = ["listen", "silent", "enlist", "hello", "loleh"]

def find_anagrams(word_list):
    anag = dict()
    for main in word_list:
        anag[main] = []
        main_sym = set()
        for sym in main:
            main_sym.add(sym)
        main_sym = sorted(list(main_sym))
        
        for word in word_list:
            word_sym = set()
            for sym in word:
                
                word_sym.add(sym)
            word_sym = sorted(list(word_sym))

            if main_sym == word_sym and main != word:
                anag[main].append(word)
    return anag
print(find_anagrams(word_list))