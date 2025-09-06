import os
os.system ("cls")

maca_kg = float(input("Quantidade de maça (kg): "))
morango_kg = float(input("quantidade de morango (kg): "))

if maca_kg <= 5:
	preco_maca =1.80
else:
	preco_maca =1.50
	
if morango_kg <= 5:
	preco_morango = 2.50
else:
	preco_morango = 2.20
	
#calculo
	
total_maca = preco_maca * maca_kg
total_morango = preco_morango * morango_kg 
total= preco_maca + preco_morango

#desconto

peso_total = maca_kg + morango_kg
if peso_total > 10 or total > 15:
	total = total * 0.90
	
#final

print(f"morango: {morango_kg}kg em R$ {total_morango}")
print(f"maça: {maca_kg}kg em para R$ {total_maca}")
print(f"total R$: {total}")

