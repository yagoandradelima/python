produto = ('Lanche', 'Refri', 'Batata', 'Bombom')
preco = (10.9, 5.40, 8.30, 3.40)
qtd = []
mult = 0
soma = 0

for i in range(0,4):
    quanti = int(input('Quantos(as) {}s você quer? '.format(produto[i])))
    qtd.append(quanti)
    mult = preco[i]*qtd[i]
    soma += mult
print()
print ('O valor total do seu pedido foi de: R$ {:.2f}'.format(soma))
print("Fim do teste")
