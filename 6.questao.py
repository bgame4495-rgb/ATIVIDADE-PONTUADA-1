import os
os.system ("cls")

nota1 = float(input(f"nota 1: "))
nota2 = float(input(f"nota2: "))

media = nota1 + nota2 /2 
 
print(f"Media {media}")
if media >= 6:
    print("Parabéns")
elif media >= 4.1 - 5.9:
    print("Recuperação ")
else:
    print("REPROVADO")