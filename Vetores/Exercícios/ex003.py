from os import system
system("cls || clear")

QUANTIDADE_NUMEROS = 6
numeros = []
par = 0
impar = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1} número: "))
    numeros.append(numero)
    
    if numero %2 == 0:
        par += 1
    else:
        impar += 1

for numero in numeros:
    print(f"Números: {numero}")

print(f"Par: {par}")
print(f"Ímpar: {impar}")
