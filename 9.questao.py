import os
os.system ("cls")


renda = float(input("Digite sua renda mensal R$: "))
emprestimo = float(input("Digite o valor do empréstimo solicitado R$: "))
prestacoes = int(input("Digite o número de prestações desejado: "))




#regra pra empretimo

limite_emprestimo = renda * 10
valor_prestacao = emprestimo / prestacoes
limite_prestacao = renda * 0.30

#resultado

if emprestimo <= limite_emprestimo and valor_prestacao <= limite_prestacao:
    print(" Empréstimo aprovado!")
    print(f"Valor do empréstimo: R$ {emprestimo:.2f}")
    print(f"Número de prestações: {prestacoes}")
    print(f"Valor de cada prestação: R$ {valor_prestacao:.2f}")
    
else:
    print("Empréstimo negado.")
    if emprestimo > limite_emprestimo:
        print(f"- O valor solicitado excede 10 vezes a renda (máximo: R$ {limite_emprestimo:.2f}).")
    if valor_prestacao > limite_prestacao:
        print(f"- O valor da prestação excede 30% da renda (máximo: R$ {limite_prestacao:.2f}).")
