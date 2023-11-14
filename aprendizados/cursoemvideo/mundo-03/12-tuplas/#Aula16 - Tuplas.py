lanche = ['hamburguer', 'suco', 'pizza', 'pudim'] #posso remover os colchetes e continuará sendo uma tupla
#Tuplas são IMUTÁVEIS!!!!!!

#Observar os resultados únicos de cada print
print (lanche)
print(lanche[0])
print(lanche[-2])
print(lanche[-1])
print(lanche[1:])
print(lanche[0:2]) #lembrar que o python sempre ignora o último elemento
print(lanche[:2]) #lembrar que o python sempre ignora o último elemento
print(lanche[-2:2]) #lembrar que o python sempre ignora o último elemento

#no FOR esse C é um variável que não precisa de atribuição, só colocar para rodar que ele passa pela tupla
for c in lanche: 
    print(f'Vou comer {c}')

#printando o tamanho da tupla
print(len(lanche))

#printando com for de maneira diferente
for cont in range(0, len(lanche)):
    #print dos números da tupla abaixo
    #print(cont)
    #print dos elementos da tupla
    print(lanche[cont])

#printando a posição e o dado da informação
for pos, comida in enumerate(lanche):
    print(f'Eu vou comera a comida {pos} - {comida}')

#Print da tupla em ordem alfabética. Muda somente esteticamente
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8 ,1 , 2)
#Soma de tuplas é concatenação
c = b + a
print(c)

#contador de vezes que um determinado número aparece
print(c.count(5))
#mostrador de posições de um elemento da tupla
#Se houver mais de um elemento ele mostra a primeira ocorrência
print(c.index(8))
print(c.index(2, 4))

#print de uma tupla com elementos diferentes
pessoa = ('Gustavo', 39, 'M', 99.98)
print('pessoa')

#eu posso deletar uma tupla, contanto que eu delete ela inteira
del(pessoa)