from os import system

# Função sem retorno.
def logoSenai():
    system("cls || clear")
    print(" === ===== === ")
    print(" === SENAI === ")
    print(" === ===== === ")

def somar(numeroPrimeiro,numeroSegundo):
    resultado = numeroPrimeiro + numeroSegundo
    return resultado

def subtrair(numeroPrimeiro,numeroSegundo):
    resultadoSubtracao = numeroPrimeiro - numeroSegundo
    return resultadoSubtracao

def multiplicar(numeroPrimeiro,numeroSegundo):
    resultadoMultiplicacao = numeroPrimeiro * numeroSegundo
    return resultadoMultiplicacao

def dividir(numeroPrimeiro,numeroSegundo):
    resultadoDivisao = numeroPrimeiro / numeroSegundo
    return resultadoDivisao

#Solicitando dados para o usuário.
logoSenai()
primeiroNumero = int(input("Digite o primeiro número: "))
logoSenai()
segundoNumero = int(input("Digite o segundo número: "))

soma = somar(primeiroNumero,segundoNumero)
subtracao = subtrair(primeiroNumero,segundoNumero)
multiplicacao = multiplicar(primeiroNumero,segundoNumero)
divisao = dividir(primeiroNumero,segundoNumero)

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisao: {divisao}")
