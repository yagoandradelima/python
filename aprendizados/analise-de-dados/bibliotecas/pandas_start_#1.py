import numpy as np
import pandas as pd

#Series é como uma linha ou coluna do DataFrame(tabela). Ele pode parecer um array do numpy, mas possui atributos diferentes
#Fazendo uma Series de passos dos meus ultimos 5 dias
steps = pd.Series([836, 856, 3775, 5747, 3311])
print(steps)
print()

print('Printando o tipo ao qual steps faz parte')
print(type(steps))
print()

print('Printando os valores de steps')
print(steps.values)
print()

print('Printando os parâmetros de formação de steps')
print(steps.index)
print()

#Mudando o tipo da index
#Visualizar que antes era 0 a 4 os índices, mas agora ficou de seg a sex
steps2 = pd.Series([325, 8874, 1256, 451, 566], index=['seg', 'ter', 'qua', 'qui', 'sex'])
print(steps2)
print()

print(steps2.index)
print()

#Funções como min, max, std, var e entre outras, podem ser utilizadas dentro de uma Series
print('O valor máximo na Series')
print(steps2.max())
print()

print('O valor mínimo na Series')
print(steps2.min())
print()

print('O valor médio da Series')
print(steps2.std())
print()

print('O valor da variação da Series')
print(steps2.var())
print()

print('Somatória dos valores da Series')
print(steps2.sum())
print()

print('Descrição completa: contador, media, desvio padrão, minimo, quartio 25%, \n quartio 50%, quartio 75%, máximo')
print(steps2.describe())
print()

print('Multiplicando os valores da Series')
print(steps2*2)
print()

print('Aplicando função numpy na series')
print(np.sqrt(steps2))
print()

