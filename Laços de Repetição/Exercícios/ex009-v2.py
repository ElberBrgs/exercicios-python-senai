soma = 0
for i in range(1,3):
    while True:
        nota = float(input("Digite uma nota: "))
    
        if nota < 0 or nota > 10:
            print("Nota inválida, digite algo entre 0 e 10.")
        else:
            soma += nota
            break

media = soma / i
print(f"Média: {media}")
