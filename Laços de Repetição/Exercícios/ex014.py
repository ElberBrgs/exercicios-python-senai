import os
os.system("clear || cls")

pares = 0
somaPares = 0
impares = 0
somaGeral = 0
contador =0

while True:
    numero = float(input("Digite um número positivo (acima de zero): "))

    if numero != 0:
        if numero > 0:
            somaGeral += numero
            contador += 1

            if numero % 2 == 0:
                somaPares += numero
                pares += 1
            else:
                impares += 1    
    else:
        break
    
mediaPares = somaPares / pares
mediaGeral = somaGeral / contador

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
print(f"Média dos pares: {mediaPares}")
print(f"Média geral: {mediaGeral}")
