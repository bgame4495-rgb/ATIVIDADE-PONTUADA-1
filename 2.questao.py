
import os
os.system("cls")

nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ")
estado_civil = input("Digite o estado civil: ")

tempo_casada = None

if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Digite o tempo de casada: "))

print("Dados do usuário")
print("Nome:", nome)
print("Sexo:", sexo)
print("Estado civil:", estado_civil)

if tempo_casada is not None:
    print("Tempo de casada:", tempo_casada, "anos")
