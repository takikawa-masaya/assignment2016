import CaboCha

sent = "豊工に行っています。"
c = CaboCha.Parser()
tree = c.parseToString(sent)
words = tree.split()
#words.pop() #リスト末尾削除

for word in words:
    print(word.replace("-D",""))
