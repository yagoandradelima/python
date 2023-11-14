l1 = [2, 6, 4, 5, 7]
print('Lista original: ', l1)

#Modificando um valor da lista
l1[2] = 3
print('Lista alterando o número na posição 2: ',l1)
print()

#Modificando um intervalo da lista
l1[0:2] = [0,1]
print('Lista modificando um intervalo de valores: ',l1)
print()

#Adicionando termos sem destacar posição
l1.append(7)
print('Lista após acrescentar mais um termo sem destacar posição: ',l1)
print()

#Adicionando termos destacando a posição
l1.insert(3, 4)
print('Inserindo o número 4 na quarta posição: ', l1)
print()

#Deletando termos da lista destacando sua posição
del l1[3]
print('Imprimindo lista após deletar um valor na posição 3: ',l1)
print()

#Salvando um termo em um var após remover ele da lista
deletado = l1.pop(2)
print(l1, ' - ',deletado)
print()

#Deletando uma variável da fila através do seu valor
l1.remove(7)
print('Deletando uma variável da fila através do seu valor: ',l1)
print()

#Evitando o erro de remover um item inexistente usando o If
if 1 in l1:
    l1.remove(1)
    print('Removendo dentro de um If: ',l1)
    print('Valor removido')
print()



l2 = [0, 3, 1, 7, 5, 7, 4]
print('Nova lista: ',l2)
print()

#Ordenando a lista com sorted
sort1 = sorted(l2)
print('Ordenando a nova lista: ',sort1)

#Ordenando com .sort
sort2 = l2.sort()
print(sort2)
print(l2)

#Ordenação inversa
l2.sort(reverse = True)
print(l2)

#Declarando lista em branco
lista1 = []

#Somando valores em uma lista em branco
for i in range(1,6):
    valor = int(input('Digite o {}º valor: '.format(i)))
    lista1.append(valor)
print()
print(lista1)
print ('testando essa porra')

#Colocando uma lista com passo de 0.1
eixox = list(range(0,100+1,1))

for i in eixox:
    eixox[i] /= 10
print(eixox)

#Clonando listas
l4 = [0, 2, 6, 4, 8, 1, 3]
l5 = l4 [:]

l4.pop()
print(l4)
print(l5)
print()
print()
print()

#Somando listas
#por causa do print que o l7 pega os valores
#o código vai listando l6 e como l7 tem o mesmo tamanho, dá pra listar l7 ao mesmo tempo
l6 = [0, 2, 6, 4, 8, 1, 3]
l7 = [3, 2, 1, 7, 8, 2, 5]
l8 = []
for i, val in enumerate(l6):
    print('l6[{}] = {} e l7[{}] = {}'.format(i, l6[i], i, l7[i]))
    l8.append(l6[i]+l7[i])
print(l8)
print()
print()
print()

#Somando listas de tamanhos diferentes
l9 = [0, 2, 6, 4, 8, 1, 3]
l10 = [3, 2, 1, 7, 8]
l11 = []

for v1, v2 in zip(l9,l10):
    print('v1 = {} e v2 = {}'.format(v1,v2))
    l11.append(v1 + v2)
print(l11)
