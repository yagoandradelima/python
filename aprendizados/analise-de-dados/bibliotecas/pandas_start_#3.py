import pandas as pd
import numpy as np

#Lembrar do formato de array ([]) << array simples onde cada valor inserido é uma coluna
array = np.array([[72, 180, 26],[80, 170, 19],[60, 165, 15]])
print(array)
print()
df = pd.DataFrame(data=array, index=['Pedro', 'Ricardo', 'Luana'], columns=['Peso', 'Altura', 'Idade'])
print(df)
print()

#Lembrar que os resultados do acesso retornam uma visulização de SERIES
print('Printando acessando os valores de uma COLUNA')
print(df['Altura'])
print()

print('Acessando uma linha')
print(df.loc['Pedro'])
print()

print('Acessando um elemento específico do dataframe')
print('A idade de Luana é', df['Idade']['Luana'], 'anos')
print()

print('Uma outra maneira de selecionar dados')
print(df.loc['Luana']['Idade'])
print()

print('Selecionando duas colunas')
print(df[['Idade', 'Peso']])
print()

print('Acessando os índices através dos números de indexação')
print(df.iloc[2][1])
print()
