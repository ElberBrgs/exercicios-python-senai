while True:
    nota = float(input("Digite uma nota: "))
    soma = 0
    contador = 0

    if nota > 0 and nota < 10:
        soma += nota
        contador +=1
    else:
        nota = float(input("Digite uma nota entre 0 e 10: "))
    if soma > 2:
        media = soma / contador
        print(f"Média: {media}")
        break
    