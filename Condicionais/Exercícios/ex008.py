

print("===MENU===")
print("Código | Prato | Valor")
print("1 - Picanha - R$ 25,00")
print("2 - Lasanha - R$ 20,00")
print("3 - Strogonoff - R$ 18,00")
print("4 - Bife acebolado - R$ 15,00")
print("5 - Pão com ovo - R$ 5,00")

codigo = int(input("Digite o código desejado: "))

match(codigo):
    case 1:
        prato = "Picanha"
        valor = float (25)
    case 2:
        prato = "Lasanha"
        valor = float (20)
    case 3:
        prato = "Strogonoff"
        valor = float (18)
    case 4:
        prato = "Bife acebolado"
        valor = float (15)
    case 5:
        prato = "Pão com ovo"
        valor = float (5)
    case _:
        print("selecione um código válido.")

print(f"Prato: {prato}")
print(f"Valor: {valor}")
