import sys
import shelve
import os
from nltk.tokenize import sent_tokenize, word_tokenize

label = sys.argv[2]
for files in os.listdir(sys.argv[1]):
    fr = open(str(sys.argv[1])+str(files)).read()
    sent = sent_tokenize(fr)

    word = []
    for sents in  sent:
        word.extend(word_tokenize(sents))

    index = shelve.open("freq_to_index_shelve.db")
    count = {}
    for aword in word:
        if aword in count:
            count[aword] += 1
        else:
            count[aword] = 1
            if not aword in index:
                index[aword] = len(index) + 1

    dic = []
    for k,v in count.items():
        dic.append([index[k],v])
    dic.sort()

    print(label+" ",end="")
    for i, c in dic:
        print(str(i)+":"+str(c)+" ", end="")

    print()
    index.close()
