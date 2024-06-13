from os import system
from dataclasses import dataclass

system("cls || clear")

QUANTIDADE_LIVROS = 2

@dataclass
class Livro:
    titulo: str
    autor: str
    paginas: int
    preco: float

livros = []

for i in range(QUANTIDADE_LIVROS):
    livro = Livro(
        titulo = input("Digite o título do livro: "),
        autor = input("Digite o autor do livro: "),
        paginas = int(input("Digite o número de páginas do livro: ")),
        preco = float(input("Digite o preço do livro: "))
    )

    livros.append(livro)

system("cls || clear")

for i in livros:
    print(f"Título: {i.titulo}")
    print(f"Autor: {i.autor}")
    print(f"Páginas: {i.paginas}")
    print(f"Preço: {i.preco}")
