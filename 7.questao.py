import os
os.system("cls")


produto =input("Nome do Produto: ")
quantidade =  int(input ("quantidade: "))
preco_unitario = float(input("preço: "))

total = quantidade * preco_unitario

#desconto
if quantidade <= 5:
    desconto = preco_unitario * 0.2
elif quantidade > 5 and quantidade <= 10:
    desconto = preco_unitario * 0.3
else: quantidade > 10
desconto = preco_unitario * 0.5 

total_para_pagar = total - desconto

print(f"produto:  {produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço: {preco_unitario}")
print(f"total: {total: .2f}")
print(f"Desconto R$:  {desconto: .2f}")
print(f"Total a pagar (desconto incluido): {total_para_pagar}") 
