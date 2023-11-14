#Aula08 - Desafio 020 - ORDEM DE APRESENTAÇÃO

from random import shuffle

n1 = input('Digite o nome do aluno: ')
n2 = input('Digite o nome do aluno: ')
n3 = input('Digite o nome do aluno: ')
n4 = input('Digite o nome do aluno: ')

alunos = [n1, n2, n3, n4]

#O Shuffle embaralha a lista, mas ele modifica diretamente a lista e não é um variável.
#ou seja, pra printar o Shuffle, é só printar a lista após a linha do shuffle.

ordem = shuffle(alunos)

print(f'A ordem será')
#Esse print já vem com a lista embaralhada
print(alunos)