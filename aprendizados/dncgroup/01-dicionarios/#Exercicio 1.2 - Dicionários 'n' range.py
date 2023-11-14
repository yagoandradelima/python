#Exercicio 1.2 - Dicionários 'n' range
pessoas = [
          {'nome':'Everton' , 'idade':29 , 'cidade':'São José'},
          {'nome':'Thiago' , 'idade':34 , 'cidade':'São Paulo'},
          {'nome':'André' , 'idade':22 , 'cidade':'Lorena'}
]

for i, p in enumerate(pessoas):
    print(f'O nome da pessoa {i+1} é {p["nome"]}')
print('-'*30)
for i, p in enumerate(pessoas):
    for k, v in p.items():
        if k == 'idade' and v < 30:
            print(f'A pessoa {i+1} tem {p["idade"]} anos. O nome dela é {p["nome"]} e mora em {p["cidade"]}')
