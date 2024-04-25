import os
os.system("clear || cls")

idade = int(input("Digite sua idade: "))

if idade <= 18 | idade > 65:
    print("Voto opcional.")
else:
    print("Voto obrigatório.")