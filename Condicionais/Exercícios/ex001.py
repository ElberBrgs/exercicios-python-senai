import os

os.system("clear || cls")

nome = str (input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
primeiraNota = float(input("Digite a primeira nota: ")) 
segundaNota = float(input("Digite a segunda nota: ")) 
terceiraNota = float(input("Digite a terceira nota: ")) 

soma = primeiraNota + segundaNota + terceiraNota
media = soma / 3

os.system("clear || cls")

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Média: {media}")

if media < 7:
    print("Reprovado.")
else :
    print("Aprovado")     