import CaboCha

sent = "豊工に行っています。"
c = CaboCha.Parser("-n1")#-n1:固有表現解析on
tree = c.parse(sent)

for i in range(tree.token_size()):
    token = tree.token(i)
    if token.ne != "O":#O:固有表現でない
        print (token.surface, token.ne)#表層、固有表現タイプ
