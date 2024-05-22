from os import system
system("cls || clear")

QUANTIDADE_NUMEROS = 5
numeros = []

while True:
    numero = int(input(f"Digite o número: "))
    if numero == 0:
        break
    numeros.append(numero)

for i,numero in enumerate(numeros):
    print(f"Número: {numero}")

maiorNumero = max(numeros)
menorNumero = min(numeros)

print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")
