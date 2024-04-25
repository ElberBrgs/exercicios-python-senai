import os
os.system("clear || cls")

nomeProduto = str(input("Digite o nome do produto: "))
quantidadeProduto = int(input("Digite a quantidade desejada do produto: "))
precoUnitario = float(input("Digite o preço unitário do produto: "))

os.system("clear || cls")

total = quantidadeProduto * precoUnitario

if quantidadeProduto <= 5:
    desconto = precoUnitario * 0.02
elif quantidadeProduto > 5 & quantidadeProduto <= 10:
    desconto = precoUnitario * 0.03
else:
    desconto = precoUnitario * 0.05

totalPagar = total - desconto

print(f"Produto: {nomeProduto}")
print(f"Valor inicial: {total}")
print(f"Valor com desconto: {totalPagar}")