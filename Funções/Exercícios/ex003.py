from os import system

QUANTIDADE_NUMEROS = 6
listaNumeros = []

def verificarPares(numeros):
    par = 0
    for numero in numeros:
        if numero %2 == 0:
            par += 1
    return par

def verificarImpares(numeros):
    impar = 0
    for numero in numeros:
        if numero %2 != 0:
            impar += 1
    return impar

def logoSenai():
    system("cls || clear")
    print(" === ===== === ")
    print(" === SENAI === ")
    print(" === ===== === ")

logoSenai()
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    listaNumeros.append(numero)

quantidadePares = verificarPares(listaNumeros)
quantidadeImpares = verificarImpares(listaNumeros)

logoSenai()
print(f"Quantidade de pares: {quantidadePares}")
print(f"Quantidade de ímpares: {quantidadeImpares}")
