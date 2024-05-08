while True:
    nota = float(input("Digite a nota: "))
    
    if nota < 0 or nota >10:
        print("Nota inválida. Digite algo entre 0 e 10.")
    else:
        print(f"Nota: {nota}")
        break
