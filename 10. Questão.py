import os
os system ("cls")


gasolina = 6.59 
alcool = 3.79

litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ") 


if tipo == "A":
    preco_litro = alcool
    if litros <= 25:
        desconto = 0.10 
    else:
        desconto = 0.20
elif tipo == "G":
    preco_litro = gasolina
    if litros <= 25:
        desconto = 0.15
    else:
        desconto = 0.30
else: 
    preco_litro = None
    desconto = 0
         

if preco_litro is not None:
    valor_bruto = litros * preco_litro
    valor_desconto = valor_bruto * desconto
    valor_final = valor_bruto - valor_desconto
    
    print(f"Combustível: {'Álcool' if tipo == 'A' else 'Gasolina'}")
    print(f"Quantidade: {litros:.2f} L")
    print(f"Preço por litro: R$ {preco_litro:.2f}")
    print(f"Valor bruto: R$ {valor_bruto:.2f}")
    print(f"Desconto: R$ {valor_desconto:.2f}")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")
else:
    print("Tipo de combustível inválido! Digite A para Álcool ou G para Gasolina.")
