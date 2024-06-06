from os import system

valorProduto = float(input('Digite o valor do produto: '))
print('1 - Pagamento à vista.\n2 - Pagamento à prazo.')
formaPagamento = int(input('Digite o código desejado: '))
system("cls || clear")

match(formaPagamento):
    case 1:
        desconto = valorProduto * 0.1
        valorTotal = valorProduto - desconto
        print(f'Valor do produto: {valorProduto}')
        print('Forma de pagamento: à vista.')
        print(f'Valor do desconto: R${desconto}')
        print(f'Total a pagar: R${valorTotal}')
    case 2:
        totalParcelas = int(input('Total de parcelas: '))
        prazo = valorProduto / totalParcelas
        valorTotal = valorProduto * totalParcelas
        print(f'Valor do produto: {valorProduto}')
        print('Forma de pagamento: à prazo.')
        print(f'Quantidade de parcelas: {totalParcelas}')
        print(f'Valor por parcela: R${prazo}')
        print(f'Valor Total: {valorTotal}')
