from os import system

def logoSenai():
    system("cls || clear")
    print(" === ===== === ")
    print(" === SENAI === ")
    print(" === ===== === ")

def mostrarTabuada(n1):
        multiplicacao = n1 * 10
        print(f" {n1} x {i+1} = {multiplicacao}")
    

logoSenai()
numero = int(input("Digite um número para tabuada: "))

logoSenai()

tabuada = mostrarTabuada(numero)