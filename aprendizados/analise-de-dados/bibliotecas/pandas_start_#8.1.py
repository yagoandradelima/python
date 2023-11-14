import numpy as np
import pandas as pd
#importando choice pra usar na coluna de COVID
from random import choice as ch

# CRIANDO UM DATAFRAME DO 0 PARA EXEMPLOS
#Montando as Series do DataFrame

#Travando para os números não ficarem mudando a cada nova execução
np.random.seed(3)
#Criando arrays com numeros aleatórios
array_Peso = np.array(np.random.randint(45, 120, 20))
array_Altura = np.array(np.random.randint(110, 210, 20))
array_Idade = np.array(np.random.randint(25, 67, 20))
choice_Covid = [ch(['SIM', 'NÃO']) for i in range(20)]
print()

#Criando um dataframe com um dos arrays para que ele se estabeleça
covid_df = pd.DataFrame(array_Peso)
#Incluindo novas colunas com seus respectivos nomes
covid_df['Peso (Kg)'] = array_Peso
covid_df['Altura (cm)'] = array_Altura
covid_df['Idade (anos)'] = array_Idade
covid_df['Teve COVID?'] = choice_Covid
#removendo a coluna inicial que foi criada para estabelecimento do DFrame
covid_df.drop([0], axis=1, inplace=True)
print(covid_df)
#Exportando para CSV
covid_df.to_csv('datasets/covid_exemplo.csv')