import os
os.system("clear || cls")

salario5k = 0
soma = 0
contador = 0
maiorIdade = 0
menorIdade = 200

while True:
    print("\nCódigo | Descrição")
    print("1 | Adicionar pessoa.")
    print("2 | Exibir resultados e sair.")

    opcao = int(input("Digite o código desejado: "))

    if opcao == 1:
        
        idade = int(input("Digite sua idade: "))
        sexo = str(input("Digite seu sexo (M/F): "))
        salario = float(input("Digite seu salário: "))
        soma += salario
        contador += 1

        sexo = sexo.upper()
        os.system("clear || cls")

        if idade > maiorIdade:
            maiorIdade = idade
        if idade < menorIdade:
            menorIdade = idade

        if sexo == "M" and salario > 5000.00:
            salario5k += 1

    mediaGeral = soma / contador
    
    if opcao == 2:
        os.system("clear || cls")
        print(f"\nMédia salarial do grupo:R$ {mediaGeral}")
        print(f"Maior idade: {maiorIdade}")
        print(f"Menor idade: {menorIdade}")
        print(f"Mulheres com salarios acima de R$ 5.000,00: {salario5k}")
        break
