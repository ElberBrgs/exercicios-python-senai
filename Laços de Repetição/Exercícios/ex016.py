from os import system
import time

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
operador = input("Digite a operação desejada: ")

resultado = 0 

while True:
    system("cls || clear")

    match(operador):
        case '+':
            resultado = a + b
            break
        case '-':
            resultado = a - b
            break
        case '*':
            resultado = a * b
            break
        case '/':
            resultado = a / b
            break
        case _:
            print("Operador inválido.")
            time.sleep(3)

if resultado:
    print(f"Resultado: {resultado}")
