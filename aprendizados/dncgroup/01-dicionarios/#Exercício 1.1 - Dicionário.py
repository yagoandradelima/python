#Exercício 1.1 - Dicionário

cardapio = {
        'lanche': 10.9,
        'batata': 5.5,
        'refri': 3.9
}

print('+'*12, 'CARDAPIO', '+'*12)
for k, v in cardapio.items():
    print(f'{k:.<25}R$ {v:5.2f}')
print('+'*36)
qtd = {}
for k in cardapio.keys():
    qtd[k] = int(input(f'Quantos(as) {k}s você quer? '))
print('+'*36)
#print(qtd)


#É muito melhor usar a função zip
#Tentei fazer um for dentro de um for, mas exige muito conhecimento da linguagem e é mais trabalhoso
soma = 0
for  v1, v2 in  zip(cardapio.values(), qtd.values()):
    soma += v1 * v2

for k, v in qtd.items():
    print(f'{v} - {k:.<20} = R$ {v * cardapio[k]:5.2f}')
print('+'*36)
print(f'O valor total da sua compra foi de R$ {soma:.2f}')