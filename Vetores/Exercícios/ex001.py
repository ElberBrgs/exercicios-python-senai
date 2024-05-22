from os import system
system("clear || cls")

notas = []
soma = 0

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)
    soma += nota

for i in range(3):
    print(f"Nota: {notas[i]}")

media = soma / 3

print(f"Média: {media}")
