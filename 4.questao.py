import os
os.system ("cls")

peso = 5 
maca = int(input (f"QUANTAS MAÇAS COMPRAR: "))


if maca <= 5:
    preco_unitario = 1.50 

else:
    preco_unitario = 1.80

valor_total = maca * preco_unitario
print(f"preço total: {valor_total:.2f}")