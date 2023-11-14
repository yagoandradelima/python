import numpy as np

#ATENÇÃO: A dimensão de um array é sua quantidade de linhas

#                       LENDO ARRAYS
#   a = np.array ([1, 2, 3])
#   ([]) - Todo Array de NumPy precisa estar dentro dessa estrutura mínima;
#        - Cada elemento dentro dele é uma linha diferente vista da seguinte maneira:
#            a = [1]
#                [2]
#                [3]
#   
#   b = np.array ([[1, 2, 3], [2, 3, 4], [5, 6, 7]])
#        - Essa array é TRIDIMENSIONAL
#        - Notar que aqui há listas dentro de uma lista;
#        - Essa array é lida da seguinte maneira:
#            b = [1 2 3]
#                [2 3 4]
#                [5 6 7] 
#

#Criando um array unidimensional
a = np.array([[1,2,3]])

#Criando um array bidimensional
b = np.array([[0, 1, 2], [3, 4, 5]])

#Printando o array
print('Printando o array A')
print(a)
print()
print('Printando o array B')
print(b)
print()

#Printando as dimensões do array
print('Printando as dimensões do array A')
print(a.ndim)
print()
print('Printando as dimensões do array B')
print(b.ndim)
print()

#Printando o formato do array (linhas, colunas)
print('Printando o formato do array A')
print(a.shape)
print()
print('Printando o formato do array B')
print(b.shape)
print()

#Printando o tamanho da array
#Mas cuidado! Pega somente o tamanho da primeira dimensão
print('Printando o tamanho da primeira dimensão do array A')
print(len(a))
print()
print('Printando o tamanho da primeira dimensão do Array B')
print(len(b))
print()

#Verificando se é uma array numpy
print('Printando o tipo do array A')
print(type(a))
print()
print('Printando o tipo do array B')
print(type(b))
print()

#Criando um novo array do 0
#np.arange(valor inicial, valor final , passo)
#Valor final = não é incluso ao final devido aos fundamentos do python
#Passo = de quanto em quanto será feita a progressão. Pode ser float!

c = np.arange(0, 100, 1)
print()
print('Printando um novo Array automatico C')
print(c)
print()

#ATENÇÃO: Um Parâmetro np.arange(5) define a seguinte situação
#  - O array vai começar no 0
#  - O array vai finalizar no 4 (lembrar que o python ignora o último número por padrão em listas e tuplas)
#  - O passo do array é 1

#Criando um novo array do 0 com limspace
#np.arange(valor inicial, valor final , quantidade de elementos, endpoint)
#Valor final = Na função array É INCLUSO o último elemento solicitado
#Quantidade de elementos no array = Quantidade de elementos que você quer que o Array possua
#endpoint = Se False, ele ignora o último elemento que eu solicitar. Por padrão ele coloca True
d = np.linspace(1, 13, 8, endpoint=False)
print(d)
print()

#Criando arrays de 1 unidimensional
e = np.ones(10)
print('Printando o array unidimensional de 1s')
print(e)
print()

#criando arrays de 1 bidimensional
e = np.ones((5,5))
print('Printando uma array bidimensional de 1s')
print(e)
print()

#Criando arrays de zeros unidimensional
f = np.zeros(10)
print('Printando o array unidimensional de 0s')
print(f)
print()

#Criando arrays de zeros bidimensionais
g = np.zeros((6,7))
print('Printando o array bidimensional de zeros')
print(g)
print()

#Criando array ou matrizes de números aleatórios
#A função random.rand retorna diversos valores aleatório de 0 a 1
#A função recebe os seguintes parâmetros (elementos da linha, quantidade de colunas)
#Não existe a necessidade desse formato para montar o shape do random.rand >>> ((5, 5))
h = np.random.rand(5, 5)
print('Printando números aletórios de 0 a 1 dentro de um formato predefinido de array')
print(h)
print()

#Criando uma matriz identidade
#np.eye(parametro unico de colunas e linhas)
#   ex.: np.eye(4) forma uma array 4x4 identidade
i = np.eye(5)
print('Printando matriz identidade')
print(i)
print()

#Criando uma matriz e montando sua diagonal principal
#Não precisa passar parâmetro de shape, a quantidade de elementos define o numero de linhas e colunas
#Forma sempre uma matriz quadrada com os outros elementos iguais a zero
j = np.diag(np.array([1, 2, 3, 4, 5]))
print(j)
print()

