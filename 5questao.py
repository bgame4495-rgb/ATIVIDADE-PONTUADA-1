import os
os.system ("cls")


valor1 = float(input("digite o valor 1: "))
valor2 = float(input("digite valor 2: "))
operacao = input("Digite qual operação usar: ")



match operacao:
    case "+":
        print({valor1} + {valor2})
    case "-":
         print({valor1} - {valor2})
    case "*":
         print(float({valor1} * {valor2}))
    case "/":
        print({valor1} / {valor2})
    
print("fim")
  


    