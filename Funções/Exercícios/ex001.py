from os import system

def logoSenai():
    system("cls || clear")
    print(" === ===== === ")
    print(" === SENAI === ")
    print(" === ===== === ")

def calcularMedia(n1,n2):
    calculoMedia = (n1 + n2) / 2
    return calculoMedia

logoSenai()
primeiroNumero = int(input("Digite um número: "))
logoSenai()
segundoNumero = int(input("Digite um número: "))

media = calcularMedia(primeiroNumero,segundoNumero)

logoSenai()
print(f"Média: {media}")
