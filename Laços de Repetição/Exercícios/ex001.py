from os import system
system("clear || cls")

numero = int(input("Digite um número: "))

for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")
    