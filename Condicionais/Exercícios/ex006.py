import os
os.system("clear || cls")

print("===Tabela de preços===")
print("---Até 5kg---")
print("Morango: R$ 2,50")
print("Maçã: R$ 1,80")
print("---Acima de 5kg---")
print("Morango: R$ 2,20")
print("Maçã: R$ 1,50\n")

quantidadeMorango = int(input("Quantos Kg de morango deseja comprar? "))
quantidadeMaca = int(input("Quantos Kg de maçã deseja comprar? "))
valorMorango: float = 2.50
valorMaca: float = 1.80
valorTotal = valorMorango + valorMaca
quantidadeFrutas = quantidadeMorango + quantidadeMaca
desconto: float

os.system("clear || cls")

print(f"Kg de morango: {quantidadeMorango}.")    
print(f"Kg de maçã: {quantidadeMaca}.")    
print(f"Peso total das frutas: {quantidadeFrutas} Kg.")    

if quantidadeFrutas >= 5:
    valorMorango = 2.20
    valorMaca = 1.50
    valorTotal = (quantidadeMorango * valorMorango) + (quantidadeMaca * valorMaca)
    print(f"Valor total: R$ {valorTotal}")

else:
    valorTotal = (quantidadeMorango * valorMorango) + (quantidadeMaca * valorMaca)
    print(f"Valor total: R$ {valorTotal}")   

if quantidadeFrutas >= 8 or valorTotal > 25.00:
    desconto = valorTotal * 0.1
    valorTotal = valorTotal - desconto
    print(f"Desconto de 10% aplicado")
