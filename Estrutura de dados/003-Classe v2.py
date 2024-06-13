from dataclasses import dataclass
from os import system

system("cls || clear")

#Constante.
QUANTIDADE_ALUNOS = 1

#Classe.
@dataclass
class Aluno:
    nome: str
    idade: int 
    
#Vetor.
alunos = []

#Solicitando dados para o usuário.
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
                nomeAluno = input("Digite seu nome: "),
                idadeAluno = int(input("Digite sua idade:"))
            )
    
    alunos.append(aluno)

system("cls || clear")

#Exibindo dados para o usuário.
for i in alunos:
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
