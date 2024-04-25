import os

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))

soma = primeiraNota + segundaNota
media = soma / 2

os.system("clear || cls")

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira Nota: {primeiraNota}")
print(f"Segunda Nota: {segundaNota}")
print(f"Média: {media}")