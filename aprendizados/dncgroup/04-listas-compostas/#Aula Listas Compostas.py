comida1 = ['lanche', 10.9]
comida2 = ['batata', 5.5]
comida3 = ['refri', 3.9]
cardapio = [comida1, comida2, comida3]
print(cardapio)
print()

#Acessando valores e seus prints
print(f'cardapio[0] = {cardapio[0]}')
print(f'cardapio[1] = {cardapio[1]}')
print(f'cardapio[2] = {cardapio[2]}')
print(f'cardapio[0][0] = {cardapio[0][0]}')
print(f'cardapio[0][1] = {cardapio[0][1]}')
print(f'cardapio[1][0] = {cardapio[1][0]}')
print()
print()


#Declarando listas de listas
lanche = ['lanche', 10.9]
batata = ['batata', 5.5]
refri = ['refri', 3.9]
cardapio1 = [lanche, batata, refri]
print(cardapio1)
print()
print(cardapio[1][0])
print()
print(f'lanche = {lanche} e cardapio1[0] = {cardapio1[0]}')
print(lanche == cardapio[0])

#Declaração direta de listas
cardapio1 = [['Lanche', 10.9], ['Batata', 5.5], ['Refri', 3.9]]
print(cardapio1)
print()
print(cardapio[0][1])

#Adicionando com .append listas em listas
cardapio2 = []
comida1 = []


comida1.append('Lanche')
comida1.append(10.9)
cardapio2.append(comida1[:]) #faz uma cópia para evitar que a limpeza limpe o cardapio2 também

comida1.clear() #limpa a variável
comida1.append('Batata')
comida1.append(3.5)
cardapio2.append(comida1[:])

comida1.clear() #limpa a variável
comida1.append('Refri')
comida1.append(4.5)
cardapio2.append(comida1[:])

print(comida1)
print(cardapio2)


#Usando estrutura de repetição
#cardapio3 = []
#comida2 = []

#for c in range (0,3):
    #comida2.append(str(input('Fale o nome do Comida: '))) #Colocando diretamente o input str na lista
    #comida2.append(float(input('Qual o valor da Comida: ')))
    #cardapio3.append(comida2[:])
    #comida2.clear() #Quando limpa-se comida, ela entra como uma nova lista em cardápio
    #print(f'no passo {c} comida = {comida2} e cardapio = {cardapio3}') #o f é o .format, mas de outra maneira. Ele busca os valores das variáveis dentro das chaves
    #print(comida2)


#Acessando valores dentro de um for
print()
for c in cardapio:
    print(f'c = {c}, c[0] = {c[0]}, c[1] = {c[1]}')#O c nesse caso já entra representando uma lista completa dentro da lista de armazenamento

