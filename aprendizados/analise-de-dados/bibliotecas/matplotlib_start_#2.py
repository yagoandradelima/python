import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.01)
y1 = np.sin(x) #Primeira linha
y2 = np.cos(x) #Segunda linha
y3 = np.sin(x) + np.sin(3*x) #Terceira linha

plt.title('Gráfico aula 2') #Titulo do gráfico
plt.xlabel('Eixo x') #Nome do eixo x
plt.ylabel('Eixo y') #Nome do eixo y
plt.grid(True) #colocando gradeamento
plt.plot(x, y1, label='Seno de x') #Plotando função 1 no gráfico 1. Colocando legenda
plt.plot(x, y2, label= 'Cosseno de x') #Plotando função 2 no gráfico 1. Colocando legenda
plt.plot(x, y3, label='Seno de x + 3*seno de x') #Plotando função 3 no gráfico 1. Colocando legenda
plt.legend(loc='upper right') #Solicitando legenda no gráfico. Mudando posicionamento (default = lower left)
plt.xticks(np.arange(0,11,1)) #Plotando os números indicadores do eixo x
plt.yticks(np.arange(-1, 4, 1)) #Plotando os números indicadores do eixo y
plt.show() #Pedindo pra mostrar o gráfico

#SUBPLOTS
#Plotagens de gráficos comparativos a partir de dados maiores
#Exemplo: as três linhas do gráfico anterior ter cada uma um gráfico para si

plt.subplot(1, 3, 1) #Legenda: plt.subplot(Número de linhas de apresentação, número de colunas de apresentação, região que quero mostrar)
plt.plot(x, y1) #Plotando dentro do subplot uma única linha
plt.subplot(1, 3, 2) #Colocando o gráfico na posição 2 das 3 disponíveis
plt.plot(x, y2)
plt.subplot(1, 3, 3) #Colocando o gráfico na posição 3 das 3 disponíveis
plt.plot(x, y3)
plt.figure(figsize=(12,6)) #Passar uma tupla (1,2) no figsize!
plt.tight_layout() #Melhora sutil no espaçamento
plt.show() #Mostrando o gráfico


