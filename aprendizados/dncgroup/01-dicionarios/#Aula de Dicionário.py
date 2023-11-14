#Declarando dicionários
lista = ['Everton', 29, 'São José']
dicio = {
            'nome': 'Everton',
            'idade': 29,
            'cidade': 'São José'
}

print(lista)
print(dicio)

#Declarando dicionário vazio
dic1 = {}
dic2 = dict()
dic3 = {
    'key1': 'value1',
    'key2': 38.5,
    'key3': True,
    'key4': [0, 1]
}
print(dic1)
print(dic2)
print(dic3)


#Acessando valores
pessoa = {
    'nome': 'Everton',
    'idade': 29,
    'cidade': 'São José'
}
print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cidade'])

#Modificando Valores
pessoa['cidade'] = 'São Paulo'

print(pessoa)

#Criando uma nova chave
pessoa['peso'] = 65 
pessoa['Cidade'] = 'São José' #Se houver um caractere diferente, ele cria uma nova chave

print(pessoa)


#Deletando uma chave com seu valor
del pessoa['Cidade']
print()
print(pessoa)

#imprimindo
print()
print()
print(pessoa)
print(pessoa.values())
print(pessoa.keys())
print(pessoa.items())
print()
print()
print()

#Dicionários dentro do for
    #Acessando valores com for
for v in pessoa.values():
    print(f'O valor v = {v}')

    #Acessando as chaves
for k in pessoa.keys():
    print(f'O valor k = {k}')

    #Acessando itens
for k, v in pessoa.items():
    print(f'O valor de k = {k} e v = {v}')
print()
print()
print()

#Dicionários dentro de listas
pessoas = [
          {'nome':'Everton' , 'idade':29 , 'cidade':'São José'},
          {'nome':'Thiago' , 'idade':34 , 'cidade':'São Paulo'},
          {'nome':'André' , 'idade':22 , 'cidade':'Lorena'}
]
print()
print(pessoas[2])

    #Imprmindo o nome da pessoa 1 (Everton)
print(pessoas[0]['nome'])

    #Imprimindo a idade da pessoa 2 (34)
print(pessoas[1]['idade'])

    #Imprimindo a cidade da pessoa 3 (Lorena)
print(pessoas[2]['cidade'])
print()
print()
    #For dentro de for
for p in pessoas:
    print(p)
    for k, v in p.items():
        print(k, v)
print()
print()
print()

#Copiando dicionários para dentro de listas
temp = {}
pessoas = []

while True:
    temp['Nome'] = str(input('Fale um nome: '))
    temp['idade'] = int(input('Fale uma idade: '))
    temp['cidade'] = str(input('Fale uma cidade: '))
    controle = str(input('Você quer continuar [s/n]? '))
    pessoas.append(temp.copy()) #Só assim que posso copiar um dicionáro para uma lista.
    #Se não copiar desse jeito, fica tudo clonando ao invés de acrescentar
    if controle == 'n':
        break
print(temp)
print(pessoas)
print('Fim')
