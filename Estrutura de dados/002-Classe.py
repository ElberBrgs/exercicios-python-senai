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
    nota: float
    altura: float
    peso: float

#Vetor.
alunos = []

#Solicitando dados para o usuário.
for i in range(QUANTIDADE_ALUNOS):
    nomeAluno = input("Digite seu nome: ")
    idadeAluno = int(input("Digite sua idade:"))
    notaAluno = float(input("Digite sua nota: "))
    alturaAluno = float(input("Digite sua altura: "))
    pesoAluno = float(input("Digite seu peso: "))

    aluno = Aluno(nome = nomeAluno, 
                  idade = idadeAluno,
                  nota = notaAluno,
                  altura = alturaAluno,
                  peso = pesoAluno)
    
    alunos.append(aluno)

system("cls || clear")

#Exibindo dados para o usuário.
for i in alunos:
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print(f"Nota: {i.nota}")
    print(f"Altura: {i.altura}")
    print(f"Peso: {i.peso}")
