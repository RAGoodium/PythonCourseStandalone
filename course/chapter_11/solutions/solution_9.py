from string import punctuation


word = dict()
bigramm = dict()
trigramm = dict()
s2 = ""
s = input().lower()

for symb in s:
    if symb not in punctuation:
        s2 = s2 + symb
s2 = s2.split()

words = list()
for w in s2:
    if w not in word:
        word[w] = 1
    else:
        word[w] += 1
    #words.append(w, ": ", word[w], sep="")
#print(word)

w2 = ""
for b in s2:
    w1 = w2
    w2 = b
    bi = w1 + " " + w2
    if w1 == "":
        continue
    else:
        if bi not in bigramm:
            bigramm[bi] = 1
        else:
            bigramm[bi] += 1
#print(bigramm)

w3 = ""
for t in s2:
    w1 = w2
    w2 = w3
    w3 = t
    tr = w1 + " " + w2 + " " + w3
    if w1 == "" or w2 == "":
        continue
    else:
        if tr not in trigramm:
            trigramm[tr] = 1
        else:
            trigramm[tr] += 1
#print(trigramm)

print('Слова:', end=" ")
for w in word:
    print(w, word[w], sep=": ", end=", ")
    #print(*words)
print()
    
print('Биграммы:', end=" ") #в фор переделать
q = ", ".join([b + ": " +str(bigramm[b])for b in bigramm])
print(q)

print('Триграммы:', end=" ")
for t in trigramm:
    print(t, trigramm[t], sep=": ", end=", ")
print()