from os import system
system("clear || cls")

soma = 0

for i in range(1,5):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma += nota
system("clear || cls")

media = soma / i
print(f"Média: {media}")
