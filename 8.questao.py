import os
os.system("cls")

cor= input("Escolha a cor desejada: ")

match cor:
	case "verde":
		print("CD da faixa verde R$:10.00")
	case "azul":
		print("CD da faixa azul R$20.00")
	case "amarelo":
		print("CD da faixa Amarela R$30.00")
	case "vermelho":
		print("CD da faixa Vermelha R$40.00")
	case _:
		print("Cor invalida")
