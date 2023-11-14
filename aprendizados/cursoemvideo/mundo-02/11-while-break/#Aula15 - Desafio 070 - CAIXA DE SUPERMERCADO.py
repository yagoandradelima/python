#Aula15 - Desafio 070
from tkinter import N
totalG = prodCaro = qtdProd = barato = 0
print('-'*20)
print('LOJAS SUPER BARATÃO')
print('-'*20)
while True:
    prodNome = str(input('Digite o nome do produto: '))
    precoProd = float(input('Digite o preço do produto: R$'))
    continua = ' '
    totalG += precoProd
    qtdProd += 1
    if precoProd > 1000:
        prodCaro += 1
    if qtdProd == 1:
        barato = precoProd
    elif qtdProd > 1:
        if precoProd < barato:
            n = prodNome
    while continua not in 'SN':
        continua = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if continua == 'N':
        break
print()
print('='*7, ' FIM DO PROGRAMA ', '='*7)
print(f'O total gasto foi R$ {totalG}')
print(f'{prodCaro} produtos custaram mais de R$ 1000,00')
print(f'O produto mais barato foi {n}')
