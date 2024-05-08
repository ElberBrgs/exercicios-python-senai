from os import system
import time
system("clear || cls")

soma = 0
contadorNotas = 0

print("===OPÇÕES===")
print("S- Inserir mais uma nota.")
print("P- Ver quantas notas foram inseridas.")
print("N- Calcular a média das notas informadas.")

while True:
    opcao = input("Insira a opção desejada: ")
    nota = float(input("Digite uma nota: "))

    opcao = opcao.upper()    
    

    if opcao == 'P':
        contadorNotas += 1
        print(f"Notas inseridas: {contadorNotas + 1}")
        break

    if opcao == 'N':
        soma += nota
        contadorNotas += 1
        break

media = soma / contadorNotas    
print(f"Média: {media}")

