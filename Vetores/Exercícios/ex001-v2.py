from os import system
system("clear || cls")

QUANTIDADE_NOTAS = 3
notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

#ForEach
for nota in notas:
    print(f"Nota: {nota}")

media = sum(notas) / QUANTIDADE_NOTAS

print(f"Média: {media}")
