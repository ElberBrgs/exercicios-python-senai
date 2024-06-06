from os import system

mes = int(input('Digite um número equivalente a um mês: '))

match(mes):

    case 1:
        system("cls || clear")
        mes = 'Janeiro'
    case 2:
        system("cls || clear")
        mes = 'Fevereiro'
    case 3:
        system("cls || clear")
        mes = 'Março'
    case 4:
        system("cls || clear")
        mes = 'Abril'
    case 5:
        system("cls || clear")
        mes = 'Maio'
    case 6:
        system("cls || clear")
        mes = 'Junho'
    case 7:
        system("cls || clear")
        mes = 'Julho'
    case 8:
        system("cls || clear")
        mes = 'Agosto'
    case 9:
        system("cls || clear")
        mes = 'Setembro'
    case 10:
        system("cls || clear")
        mes = 'Outubro'
    case 11:
        system("cls || clear")
        mes = 'Novembro'
    case 12:
        system("cls || clear")
        mes = 'Dezembro'
    case _:
        mes = 'Mês inexistente'

print(f'Mês: {mes}.')
