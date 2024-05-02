import os
os.system("clear || cls")

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo: ")
estadoCivil = input("Digite seu estado civil: ")

os.system("clear || cls")

estadoCivil = estadoCivil.capitalize()
sexo = sexo.upper()

if sexo == "F" and estadoCivil == "Casada":
    tempoCasada = int(input("Digite há quantos anos está casada: "))
    print(f"Nome: {nome}")
    print(f"Sexo: {sexo}")
    print(f"Estado civil: {estadoCivil}.")
    print(f"Casada há: {tempoCasada} anos.")
    
else:
    print(f"Nome: {nome}")
    print(f"Sexo: {sexo}")
    print(f"Estado civil: {estadoCivil}.")
