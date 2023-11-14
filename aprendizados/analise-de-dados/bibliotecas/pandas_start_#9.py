import pandas as pd
import numpy as np

#fazendo um array simples indo 1 até 10 com passo de 1 em 1
array = np.arange(1, 10, 1).reshape(3, 3)

#Fazendo 3 DataFrames diferentes para realizar a junção
df1 = pd.DataFrame(array, columns='A B C'.split())
df2 = pd.DataFrame(array, columns='A B C'.split())
df3 = pd.DataFrame(array, columns='G H I'.split())

#Quando quero unir dataframes (colocando um ao lado ou abaixo do outro)
#usar a função concat

#Ao realizar esse print, o python reconhece que as colunas tem o mesmo nome e coloca um abaixo do outro
#Mas é bom observar que os índices se repetem!
#pra isso é necessário utilizar o ignore_index=True
print(pd.concat([df1, df2], ignore_index=True))
print()

#concatenando por colunas utilizando o axis=1
print(pd.concat([df1, df3], axis=1))
print()

#concatenando tudo
print(pd.concat([df1, df2, df3], ignore_index=True))
print()

#usando a função merge
#essa função mescla uma coluna e junta os DataFrames
#A coluna precisa ser igual no nome e no conteúdo em ambos os DataFrames

df4 = pd.DataFrame(array, columns='D B C'.split())

print(pd.merge(df1, df4, on=['B','C']))
print()

#Usando JOIN
#Criando dois DataFrames com índices diferentes
#Isso impede o uso do concat
df5 = pd.DataFrame(array, columns='A B C'.split(), index=[0, 1, 2])
df6 = pd.DataFrame(array,columns='D E F'.split(), index=[1, 2, 3]) 

#Por padrão o default é left join, ou seja, ele pega por completo os índices do DF à esquerda e
#caso o da direita não tenha Indices com os mesmos labels, então os que não são iguais são ignorados
#Exemplo: df5 join df6, perceber no result set que os índices dessa visualiação são 0 1 2.
#Caso how='right', então os índices de df6 1 2 3 serão mostrados por completo e indices com labels diferentes
#no df5 vão ser ignorados.
print(df5.join(df6))
print()
#Para printar todos os índices
print(df5.join(df6, how='outer'))

