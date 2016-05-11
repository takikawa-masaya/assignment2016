import sys
import gzip
import nltk

jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^!?。]*[!?。]?')

line = gzip.open(sys.argv[1], "rt").readline().strip()

print(jp_sent_tokenizer.tokenize(line))
