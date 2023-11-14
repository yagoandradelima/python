import pandas as pd
import numpy as np

d = {'Python': 10, 'Matlab' : 9.7, 'javaScript': 9}

print('Printando um dicionário dentro de um Series')
series = pd.Series(d)
print(series)
#Se eu tiver uma variável float declarada na lista/dicionario/tupla
#mesmo que eu coloque dtype=int, ele vai voltar a ser float

print('Criando uma Series do 0')
#Usei o split pra dividir cada letra do index por cada espaço existente entre as letras
np.random.seed(2)
s = pd.Series(data=np.random.randint(1, 5, 10), index='A B C D E F G H I J'.split())
print(s)

print('É possível acessar um valor pelo index padrão do Python ou pelo index que eu criei')
print(s[0])
print(s['A'])
print()

print(s[2:4])
print(s['C':'D'])
print()

print(series['Python':'javaScript'])
print()

#Realizando operações com Series
r = pd.Series(data=np.random.randint(1, 100, 3), index='Facebook Instagram Twitter'.split())
t = pd.Series(data=np.random.randint(1, 100, 3), index = 'Zoom Instagram Facebook'.split())
print(r)
print()

print(t)
print()

print('Printando soma de r e t')
print(r + t)
print()

print('Printando a divisão de r e t')
print(r / t)
print()

print('Printando a subtração de r e t')
print(r - t)
print()

print('Printando a multiplicação de r e t')
print(r * t)
print()

#Vale lembrar que quando dois índices não estão presentes em
#ambas as Series o resultado retorna NaN

print('Printando máscaras')
#máscaras são slices com condições
#no caso abaixo eu queria um slice de valores maiores ou iguais a 2
print(s[s >= 2])
print()

print(s[s >= 2].index) #retorna somente o index
print()