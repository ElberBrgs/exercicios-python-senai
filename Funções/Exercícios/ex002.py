from os import system

def logoSenai():
    system("cls || clear")
    print(" === ===== === ")
    print(" === SENAI === ")
    print(" === ===== === ")

def mostrarTabuada(n1):
    for i in range(1,11):
        multiplicacao = n1 * i
        print(f" {n1} x {i} = {multiplicacao}")
    
logoSenai()
numero = int(input("Digite um número para tabuada: "))

logoSenai()
tabuada = mostrarTabuada(numero)
