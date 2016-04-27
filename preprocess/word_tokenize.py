import sys
from nltk.tokenize import sent_tokenize, word_tokenize

fr = open(sys.argv[1]).read()
sent = sent_tokenize(fr)

word = []
for sents in  sent:
    word.extend(word_tokenize(sents))

print(word)
