import os

primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

os.system("clear || cls")

soma = primeiroNumero + segundoNumero
subtracao = primeiroNumero - segundoNumero
multiplicacao = primeiroNumero * segundoNumero
divisao = primeiroNumero / segundoNumero 

print(f"Primeiro número: {primeiroNumero}")
print(f"Segundo número: {segundoNumero}")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")