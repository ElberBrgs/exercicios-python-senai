from os import system
system("clear || cls")

soma = 0

for i in range(1,4):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma += nota
system("clear || cls")

media = soma / i
print(f"Média: {media}")

if media >= 7:
    print("Aprovado.")
elif media >=5:
    print("Recuperação.")
else:
    print("Reprovado.")
