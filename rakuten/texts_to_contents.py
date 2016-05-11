import sys
import gzip
import nltk
import shelve
import MeCab

jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^!?。]*[!?。]?')
m = MeCab.Tagger()
m.parse("")

line = gzip.open(sys.argv[1], "rt").readlines()

for aline in line:
    #文分割                                                                          
    sent = jp_sent_tokenizer.tokenize(aline.strip())

    #単語分割                                                                        
    word = []
    for asent in sent:
        node = m.parseToNode(asent)
        node = node.next

        while node:
            if node.feature.split(",")[0] in [u"名詞", u"動詞", u"形容詞", u"形容動詞", u"副詞"]:
                word.extend(node.surface)
            node = node.next

    #辞書                                                                            
    index = shelve.open("rakuten_reviews_contents.db")
    count = {}
    for aword in word:
        if aword in count:
            count[aword] += 1
        else:
            count[aword] = 1
            if not aword in index:
                index[aword] = len(index) + 1

    #素性ベクトル[インデックス,頻度]                                                 
    fv = []
    for k,v in count.items():
        fv.append([index[k],v])
    fv.sort()

    for i, c in fv:
        print(str(i)+":"+str(c)+" ", end="")

    print()
    index.close()
