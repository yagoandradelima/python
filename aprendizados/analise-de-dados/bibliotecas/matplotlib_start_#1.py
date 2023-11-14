import numpy as np
import matplotlib.pyplot as plt

array = np.arange(6)
#Por padrão os valores de um array unicos se tornan valores de y
#o matplotlib.pyplot faz eles terem valores iguais no eixo x e transforma o gráfico para um formato quadrado
#do tipo y = x 
plt.plot(array)
plt.show()

#Valores com inicio e fim definidos de um array geram resultados no seguinte formato:
# y = x-1
array2 = np.arange(1, 4)
plt.plot(array2)
plt.show()

#
x = np.arange(0, 10, 0.2)
y = np.sin(x)
plt.plot(x, y)
plt.title('Seno')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)
plt.show()