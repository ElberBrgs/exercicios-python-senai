diaSemana = int(input("Digite o dia da semana (1~7): "))

match(diaSemana):
    case 1:
        print("Domingo - Fim de semana")
    case 2:
        print("Segunda-feira - Dia útil")
    case 3:
        print("Terça-feira - Dia útil")
    case 4:
        print("Quarta-feira - Dia útil")
    case 5:
        print("Quinta-feira - Dia útil")
    case 6:
        print("Sexta-feira - Dia útil")
    case 7:
        print("Sábado - Fim de semana")
    case _:
        print("Dia inválido.")
