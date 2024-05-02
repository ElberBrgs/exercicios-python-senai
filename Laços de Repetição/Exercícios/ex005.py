from os import system
system("clear || cls")

par = 0
impar = 0

for i in range(1,6):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
        
system("clear || cls")

print(f"Pares: {par}")
print(f"Ímpares: {impar}")
