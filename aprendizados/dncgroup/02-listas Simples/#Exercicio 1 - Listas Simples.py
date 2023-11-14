preco = (10.9, 5.40, 8.30, 3.40)
qtd = [0, 3, 2, 4]
mult = 0
soma = 0

for i, val in enumerate(qtd):
    mult = preco[i]*qtd[i]
    print('Valor do produto = {}. Sua quantidade foi = {}. Valor total: R$ {:.2f}'.format(preco[i],qtd[i],mult))
    soma += mult
print('Valor final = R$ {:.2f}'.format(soma))
print()
print('Fim do programa')