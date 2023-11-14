comida1 = ['lanche', 10.9]
comida2 = ['batata', 5.5]
comida3 = ['refri', 3.9]
cardapio = [comida1, comida2, comida3]

print('-'*35)
print('-'*12, 'CARDÁPIO', '-'*12)
print('-'*35)
for c in cardapio:
    print(f'{c[0]} ----------------- R$ {c[1]}')
