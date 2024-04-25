import os
os.system("clear || cls")

loginValido: str = "Elbo"
senhaValida: str = "123"

login = str(input("Login: "))
senha = str(input("Senha: "))

if login == loginValido and senha == senhaValida:
    print("Bem-vindo!")
else:
    print("Login ou senha inválidos.")