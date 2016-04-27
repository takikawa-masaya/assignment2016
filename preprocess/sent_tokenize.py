import sys
from nltk.tokenize import sent_tokenize

fr = open(sys.argv[1]).read()
print(sent_tokenize(fr))

