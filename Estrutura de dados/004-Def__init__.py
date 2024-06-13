from dataclasses import dataclass
from os import system

system("cls || clear")

#Constante.
QUANTIDADE_ALUNOS = 1

#Classe.
@dataclass
class Aluno:
    def __init__(self,nome_qualquer,idade_qualquer):
        self.nome = nome_qualquer
        self.idade = idade_qualquer 
    
#Vetor.
alunos = []

#Solicitando dados para o usuário.
for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    alunos.append(Aluno(nome,idade))

system("cls || clear")

#Exibindo dados para o usuário.
for i in alunos:
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
