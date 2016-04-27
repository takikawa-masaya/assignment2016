import MeCab

sent = "豊工に行っています。"
m = MeCab.Tagger()
print(m.parse(sent))
