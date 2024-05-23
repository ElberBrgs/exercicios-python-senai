from os import system

def logoSenai():
    system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

logoSenai()
valorProduto = float(input("Digite o valor do produto: "))

def inflacionar(valor):
    if valor < 100:
        valorProduto = (valor * 0.1) + valor
    if valor >= 100:
        valorProduto = (valor * 0.2) + valor
    return valorProduto

valorInflacionado = inflacionar(valorProduto)

logoSenai()
print(f"Valor: R$ {valorProduto}")
print(f"Valor Inflacionado: R$ {valorInflacionado}")
