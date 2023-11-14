import numpy as np
import matplotlib.pyplot as plt
import skimage as skim

#Criando um array simples de 1's
a1 = np.ones(10)
#printando o array
print (a1)
print()

#Criando um array randomico
#randint possui os parametros: (inicio do intervalo possível de escolha, fim do intervalo de escolha, qtd de números que serão sorteados)
#random.seed TRAVA o aleatório do randint como se fosse uma seed de mapa. Posso rodar várias vezes que vai se repetir.
np.random.seed(44)
a2 = np.random.randint(1, 20, 6)

#Operações com Array
mult = a1 * 10
div = a1 / 2
soma = a1 + 4
sub = a1 - 6
sqrt = a1**2

print('Multiplicando array por 10')
print(mult)
print()

print('Dividindo array por 2')
print(div)
print()

print('Somando array com 4')
print(soma)
print()

print('Subtraindo 6 do array')
print(sub)
print()

print('Elevando ao quadrado')
print(sqrt)
print()

print('Printando um array aleatório com valores em um intervalo adicionado')
print (a2)
print()
#Operações entre arrays
#No Python, o que vem embaixo no codigo vem depois, então esse seed não interfere no de cima
np.random.seed(12)
a3 = np.random.randint(12, 44, 6)

print('Printando um novo array')
print(a3)

print('Somando arrays')
#lembrar que as operações não funcionam com arrays de tamanhos diferentes
#exceção à multiplicação de matrizes
print(a2+a3)
print()

print('Multiplicando Arrays')
print('ATENÇÃO: isso é uma multiplicação elemento a elemento e não multiplicação de matrizes')
print(a2*a3)
print()

print('Subtração de arrays')
print(a2-a3)
print()

print('Divisão de arrays')
print(a2/a3)
print()



#Para realizar uma multiplicação entre matrizes existe uma regra
#A quantidade de linhas de uma matriz tem que possuir o mesmo número de colunas da segunda


#Travando a matriz em uma seed
np.random.seed(2)
#Criando uma matriz, perceba que ao final coloquei o shape pra fazer ela ser bidimensional
n1 = np.random.randint(1,16,(2,4))
#travando matriz 2 em uma seed
np.random.seed(3)
#Criando uma matriz bidimensional. Perceber que linhas e colunas coincidem entre si
n2 = np.random.randint(1, 16, (4,1))

print('Matriz n1')
print(n1)
print()
print('Matriz n2')
print(n2)
print()

#multiplicando as matrizes
print('Multiplicando matrizes')
#Como coloquei n1...(n2) então, para esse caso, a COLUNA do shape declarado de N1,
#precisa ser igual à LINHA do shape declarado em N2. Caso fosse n2...(n1), o 
#inverso deveria ser verdade
print(n1.dot(n2))
print()

#Comparando arrays
print('Comparando elemento a elemento')
r1 = np.array([1, 2, 3])
r2 = np.array([3, 2, 3])
print(r1 == r2)
print()

print('Comparando a igualdade de dois arrays completos')
print(np.array_equal(r1,r2))
print()

print('Seno de r1')
print(np.sin(r1))
print()

#Printando uma multiplicação dentro de um slice
#Se a documentaçãod do numpy pedir "defined axis"
#É só definir um slice na matriz daquilo que você quer ver
print('Printando um produto entre determinados elementos do array')
print(np.prod(n1[0,0:2]))
print()

#printando o desvio padrão
print('Desvio padrão de um array')
print(np.std(a1))
print()