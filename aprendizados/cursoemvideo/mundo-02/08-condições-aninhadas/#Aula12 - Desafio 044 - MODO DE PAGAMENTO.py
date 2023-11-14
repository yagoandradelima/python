#Aula012 - Desafio 044 - MODO DE PAGAMENTO

from math import prod

#A última opção precisa aceitar mais de 3x no parcelamento TAMBÉM
#Meu código está levemente diferente. O dele tem menu bem estruturado
#Em compensação, eu restrinjo mais erros de usuário e impeço inputs desnecessários

prodPreco = float(input('Digite o valor do produto: R$ '))
condPagt = str(input('Qual a forma de pagamento? ')).strip()


if condPagt.upper() == 'À VISTA' or condPagt.upper() == 'A VISTA':
    condPagt2 = str(input('Forma de pagamento à vista solicitada. Com qual meio de pagamento deseja prosseguir? ')).strip()

    if condPagt2.upper() == 'DINHEIRO' or condPagt2.upper() == 'CHEQUE':
        desc = prodPreco * 0.1
        prodPreco -= desc
        print('O meio de pagamento selecionado foi: DINHEIRO/CHEQUE')
        print(f'O Preço final do produto é: R$ {prodPreco:.2f}')

    elif condPagt2.upper() == 'CARTAO' or condPagt2.upper() == 'CARTÃO':
        desc = prodPreco * 0.05
        prodPreco -= desc
        print('O meio de pagamento selecionado foi: CARTÃO')
        print(f'O Preço final do produto é: R$ {prodPreco:.2f}')
    
    else:
        print('Não reconheci seu meio de pagamanto. Por favor, tente novamente')


elif condPagt.upper() == 'CARTAO' or condPagt.upper() == 'CARTÃO':
    condPagt2 = str(input('Forma de pagamento CARTÃO solicitada. Deseja parcelar de quantas vezes? '))

    if condPagt2.upper() == '2' or condPagt2.upper().split() == '2X':
        parcela = prodPreco / 2 
        print('Parcelamento de 2x foi selecionado.')
        print(f'O valor final do produto é: R$ {prodPreco:.2f}')
        print(f'O valor da parcela é = R$ {parcela:.2f}')
    
    elif condPagt2.upper() == '3' or condPagt2.upper().split() == '3X':
        desc = prodPreco * 0.2
        prodPreco += desc
        parcela = prodPreco / 3
        print('Parcelamento de 3x foi selecionado.')
        print(f'O valor total final do produto ficou: R$ {prodPreco:.2f}')
        print(f'O valor da parcela é = R$ {parcela:.2f}')

else:
    print('Não consegui compreender esta opção. Por favor, tente novamente.')

print()
print('Fim do programa')
