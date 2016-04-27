import sys
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import SennaTagger

fr = open(sys.argv[1]).read()
sent = sent_tokenize(fr)
aword = word_tokenize(sent[0])

tagger = SennaTagger('/usr/share/senna-v2.0')

for w, t in tagger.tag(aword):
    print(w, t)
