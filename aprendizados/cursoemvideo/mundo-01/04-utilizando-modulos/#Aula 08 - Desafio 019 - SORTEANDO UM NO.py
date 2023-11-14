#Aula 08 - Desafio 019 - SORTEANDO UM NOME
#Incrementei um pouco mais esse código

import random

x = ('Lucas', 'Mateus', 'Corno', 'Aluno', 'Eu')

for i in x:
    print(i)
    k = random.choice(x)
print()
print(f'Esse é o aluno escolhido aleatoriamente: {k}')