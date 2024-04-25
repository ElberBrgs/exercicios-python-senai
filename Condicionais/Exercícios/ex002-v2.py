import os

os.system("clear || cls")

primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))
menorValor: int
maiorValor: int

os.system("clear || cls")

soma = primeiroNumero + segundoNumero
produto = primeiroNumero * segundoNumero
media = soma / 2

maiorValor = max(primeiroNumero,segundoNumero)
menorValor = min(primeiroNumero,segundoNumero)

print(f"Média: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Menor valor: {menorValor}")
print(f"Maior valor: {maiorValor}")