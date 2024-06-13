from os import system
from dataclasses import dataclass

system("cls || clear")

QUANTIDADE_PETS = 1

@dataclass
class Pet:
    def __init__(self,nome,idade,raca,porte,alimentacao):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.alimentacao = alimentacao

pets = []

for i in range(QUANTIDADE_PETS):
        nome = input("Digite o nome do seu pet: ")
        idade = int(input("Digite a idade do seu pet: "))
        raca = input("Digite a raça do seu pet: ")
        porte = input("Digite o porte do seu pet: ")
        alimentacao = input("Digite a alimentação que seu pet recebe: ")
    
        pets.append(Pet(nome,idade,raca,porte,alimentacao))

system("cls || clear")

for i in pets:
     print(f"Nome: {i.nome}")
     print(f"Idade: {i.idade}")
     print(f"Raca: {i.raca}")
     print(f"Porte: {i.porte}")
     print(f"Alimentacao: {i.alimentacao}")
