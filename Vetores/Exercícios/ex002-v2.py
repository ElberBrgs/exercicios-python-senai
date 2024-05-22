from os import system
system("cls || clear")

QUANTIDADE_NUMEROS = 5
numeros = []

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

for i,numero in enumerate(numeros):
    print(f"Número: {numero}")

maiorNumero = max(numeros)
menorNumero = min(numeros)

print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")
