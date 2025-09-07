import os
os.system ("cls")



valor1 = int(input("digite o valor 1: "))
valor2 = int(input("digite valor 2: "))
operacao = input("Digite qual operação usar: ")

 


if operacao == "+":
    	resultado = valor1 + valor2 
elif operacao == "-":
    	resultado = valor1 - valor2
elif operacao == "*":
    	resultado = valor1 * valor2
elif operacao == '/':
       resultado = valor1 / valor2
else:	
	    print("operacao invalida")
	    resultado = 0
    
print(f"resultado: {resultado}")




    
