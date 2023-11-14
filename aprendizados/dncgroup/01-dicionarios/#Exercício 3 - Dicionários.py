produtos = [{
                'produto': 'maça',
                'preco': 2.2
            },
            {
                'produto': 'banana',
                'preco': 1.2
            }]
everton = {
            'cliente': 'Everton',
            'compra':[{
                        'produto': 'maça', 
                        'qtd': 3
                        },
                        {
                        'produto': 'banana',
                        'qtd' : 10} 
                        ]}

#produtos é uma lista onde suas posições são dicionários
#everton é um dicionário onde a chave compra possui uma lista com dicionários dentro

#print(produtos)
print()
#print(produtos[0])
print()
#print(produtos[0]['preco'])
print()
nomeUsuario = everton['cliente']
precoProduto = produtos[0]['preco']
precoProduto1 = produtos[1]['preco']
#print(precoProduto)
#print(precoProduto1)
print()
prodComp = everton['compra'][0]['produto']
prodComp1 = everton['compra'][1]['produto']
quantidade = everton['compra'][0]['qtd']
quantidade1 = everton['compra'][1]['qtd']
print()
#print(quantidade) #peguei a quantidade
#print(quantidade1['qtd'])
print()

media = (precoProduto+precoProduto1)/2
vParcial = precoProduto * quantidade
vParcial1 = precoProduto1 * quantidade1
vTotal = vParcial + vParcial1

print(f'A Média dos preços dos produtos é R${media:.2f}')
print()
print(f'O cliente {nomeUsuario} comprou {quantidade} {prodComp}(s) e {quantidade1} {prodComp1}(s)')
print()
print(f'O valor total da compra foi R${vTotal:.2f}')



