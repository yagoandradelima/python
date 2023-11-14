comida1 = ['lanche', 10.9]
comida2 = ['batata', 5.5]
comida3 = ['refri', 3.9]
cardapio = [['lanche', 10.9], ['batata', 5.5], ['refri', 3.9]]

quantidade = 0
soma = 0
mult = 0

print('-'*35)
print('-'*12, 'CARDÁPIO', '-'*12)
print('-'*35)
for c in cardapio:
    print(f'{c[0]} ----------------- R$ {c[1]}')
    quantidade = int(input('Quantos desse item você deseja? '))
    preco = float(c[1])
    mult = quantidade * preco
    soma += mult
print()
print(f'O valor total do seu pedido é R$ {soma}')
