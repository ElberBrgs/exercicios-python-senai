soma = 0

for i in range(1,4):
    while True:
        nota = float(input(f"Digite a {i}ª nota:"))

        if nota <0 or nota >10:
            print("Nota inválida, digite algo entre 0 e 10")
        else:
            soma += nota
            break

media = soma / i
print(f"Média: {media}")

if media >=7:
    print("Aprovado.")
elif media >=5:
    print("Recuperação.")
else:
    print("Reprovado.")
