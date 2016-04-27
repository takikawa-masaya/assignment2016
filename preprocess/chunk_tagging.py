import sys
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import SennaChunkTagger

ctagger = SennaChunkTagger('/usr/share/senna-v2.0')

fr = open(sys.argv[1]).read()
sent = sent_tokenize(fr)

aword = word_tokenize(sent[0])

print(ctagger.tag(aword))

for word, tag in ctagger.tag(aword):
    if "B-" in tag:
        print()
        print(str(tag).replace("B-",""), word, end="")

    elif "I-" in tag:
        print("", word, end="")
