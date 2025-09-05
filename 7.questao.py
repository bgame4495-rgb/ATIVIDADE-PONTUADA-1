


produto =input("Nome do Produto: ")
quantidade =  input ("quantidade: ")
preco_unitario = float(input("preço: "))

total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = preco_unitario * 0.2
elif quantidade > 5 and quantidade <= 10:
    desconto = preco_unitario * 0.3
else: quantidade > 10
desconto = preco_unitario * 0.5 