from os import system
system("cls || clear")
import sys

maiorNumero = 0
menorNumero = sys.maxsize
QUANTIDADE_NUMEROS = 5
numeros = []

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    if numero > maiorNumero:
        maiorNumero = numero
    if numero < menorNumero:
        menorNumero = numero

for numero in numeros:
    print(f"Número: {numero}")

print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")
