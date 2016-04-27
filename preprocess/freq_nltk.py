import sys
from nltk.tokenize import sent_tokenize, word_tokenize

fr = open(sys.argv[1]).read()
sent = sent_tokenize(fr)

word = []
for sents in  sent:
    word.extend(word_tokenize(sents))

dic = {}
for aword in word:
    if aword in dic:
        dic[aword] += 1
    else:
        dic[aword] = 1

ndic = [(v,k) for k,v in dic.items()]
ndic.sort()
ndic.reverse()

for c, w in ndic[:10]:
    print(c, w)
