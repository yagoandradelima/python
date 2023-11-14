#Exercicio 1.2 - Dicionários
pessoas = [
          {'nome':'Everton' , 'idade':29 , 'cidade':'São José'},
          {'nome':'Thiago' , 'idade':34 , 'cidade':'São Paulo'},
          {'nome':'André' , 'idade':22 , 'cidade':'Lorena'}
]

#Usar o range para pode usar o pessoa[0] pra acessar a linha
#Mas meu código tem limite no range. E seu tiver um range desconhecido?
for l in range(0,3):
    n = pessoas[l]['nome']
    print(f'O nome da pessoa {l+1} é: {n}')
print()
for l in range(0,3):
    r = pessoas[l]['idade']
    if r < 30:
        a = pessoas[l]['nome']
        b = pessoas[l]['cidade']
        print(f'A pessoa {a} tem {r} anos de idade e mora em {b}')

    #print(pessoas[p]['nome'])