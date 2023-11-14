# Exercício 3 - Tupla
t1 = ('Doce', 2.3, 'Bala', 0.15, 'Pizza', 28.9, 'Arroz', 4.5, 'Paçoca', 0.5, 'Pamonha', 5.4)
soma = 0    
continua = 's'
print('-'*32)
print('-'*10, ' CARDÁPIO ', '-'*10)
print('-'*32)
print('{}.....................R$ {:.2f}'.format(t1[0],t1[1]))
print('{}.....................R$ {:.2f}'.format(t1[2],t1[3]))
print('{}....................R$ {:.2f}'.format(t1[4],t1[5]))
print('{}....................R$ {:.2f}'.format(t1[6],t1[7]))
print('{}...................R$ {:.2f}'.format(t1[8],t1[9]))
print('{}..................R$ {:.2f}'.format(t1[10],t1[11]))
continua = input('Você deseja continuar [s/n]? ')
while continua == 's':
  pedido = input('O que você gostaria de pedir? ')
  posPedido = t1.index(pedido)
  posPedido += 1
  soma += t1[posPedido]
  print()
  continua = input('Você deseja continuar [s/n]? ')
print('O valor total do que você pediu é R$ {:.2f} '.format(soma))
print()
print('Fim')


  #valor += valorpedido
  #print(posPedido)