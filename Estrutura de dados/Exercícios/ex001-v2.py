from os import system
from dataclasses import dataclass

system("cls || clear")

QUANTIDADE_LIVROS = 1

@dataclass
class Livro:
    def __init__(self,titulo,autor,paginas,preco):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.preco = preco

livros = []

for i in range(QUANTIDADE_LIVROS):
    
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        paginas = int(input("Digite o número de páginas do livro: "))
        preco = float(input("Digite o preço do livro: "))
    
        livros.append(Livro(titulo,autor,paginas,preco))

system("cls || clear")

for i in livros:
    print(f"Título: {i.titulo}")
    print(f"Autor: {i.autor}")
    print(f"Páginas: {i.paginas}")
    print(f"Preço: {i.preco}")
