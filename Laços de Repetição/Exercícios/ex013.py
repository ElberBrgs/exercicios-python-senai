import os
import time
os.system("clear || cls")

soma = 0
contador = 0

while True:
    numero = float(input("Digite um número positivo: "))

    if numero >= 0:
        soma += numero
        contador += 1
    else:
        if contador == 0:
            print("Digite um número positivo inicialmente.")
            time.sleep(3)
            os.system("clear || cls")
        else:
            break

media = soma / contador
print(f"Média: {media}")
