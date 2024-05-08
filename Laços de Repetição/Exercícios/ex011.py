soma = 0
contadorNotas = 0

while True:
    nota = float(input("Digite uma nota: "))
    resposta = input("Deseja inserir mais uma nota? ")

    resposta = resposta.upper()

    if resposta != 'N':
        soma += nota
        contadorNotas += 1
    else:
        break

media = soma / contadorNotas

print(f"Média: {media}")
