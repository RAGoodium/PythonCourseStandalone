word_list = ["listen", "silent", "enlist", "hello", "loleh"]

def find_anagrams(word_list):
    anag = dict()
    for word in word_list:
        if word not in anag:
            anag[word] = []

        syms = set()
        for sym in word:
            syms.add(sym)
        
        
#начальное слово "a"
#for n in a:
#   a ^ n
      
print(find_anagrams(word_list))