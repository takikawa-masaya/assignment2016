import MeCab

sent = "豊工に行っています。"
m = MeCab.Tagger()
m.parse("")
node = m.parseToNode(sent)

node = node.next
while node:
    nf = node.feature.split(',')
    print(node.surface, nf[0], nf[6])
    node = node.next
