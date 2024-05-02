from os import system
system("clear || cls")

soma = 0

for i in range(1,6):
    numero = int(input("Digite um número: "))
    soma += numero

print(soma)
