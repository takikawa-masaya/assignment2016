import sys
import shelve
from nltk.tokenize import sent_tokenize, word_tokenize

fr = open(sys.argv[1]).read()
sent = sent_tokenize(fr)

word = []
for sents in  sent:
    word.extend(word_tokenize(sents))

index = shelve.open("freq_to_index_shelve.db")
dic = {}
for aword in word:
    if aword in dic:
        dic[aword] += 1
    else:
        dic[aword] = 1
        index[aword] = len(dic)

ndic = [(v,k) for k,v in index.items()]
ndic.sort()

for i, w in ndic[:10]:
    print(i, w)

index.close()
