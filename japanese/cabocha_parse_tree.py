import CaboCha

sent = "豊工に行っています。"
c = CaboCha.Parser()
tree = c.parseToString(sent)

print(tree)
