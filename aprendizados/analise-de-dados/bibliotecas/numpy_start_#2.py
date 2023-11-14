import numpy as np
import skimage as skm
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Criando uma Array simples com arange
print('Criando um array unidimensional')
a = np.arange(0, 11, 1)
print(a)
print()

#Acessando elementos definidos na lista
print('Acessando array unidimensional')
print(a[2])
print(a[-1])
print()

#Criando um array bidimensional
print('Criando um array bidimensional')
b = np.random.rand(5, 5)
print(b)
print()

#Acessando array bidimensional
#lembrar que coluna e linha começa na contagem 0
#também funciona se eu fizer b[1][4]
print('Acessando array bidimensional')
print(b[1, 4])
print()

#Alterando uma array
print('Alterando array b')
b[1, 4] = 22
print(b)
print()

#Fatiando um array
print('Printando da posição 2 até a 4')
print(a[2:5])
print()

print('Printando sem definir o final ou o inicio')
print(a[:5])
print(a[1:])
print()



#Fatiando um array bidimensional
#b[0:2 - fatiando as linhas
#, 2]  - fatiando valores das colunas das linhas selecionadas
print(b[0:2, 2])
print()


#Carregando uma imagem
#lembrar que img é o nome da variável
img = mpimg.imread('C:/Users/yandrade/Documents/GitHub/bibliotecas-python/imagens/d.jpg')

#printando o shape da imagem
print('Shape da imagem')
print(img.shape)
print()

print('Print da imagem unicamente')
print(img)
print()

#Pra imagem aparecer precisa de um plt.show() no final
print('tentando plotar a imagem')
plt.imshow(img)
plt.show()
print()

#Slice em uma imagem
#As imagens são arrays de pixels. Apenas solicitei que uma nova variável armazenasse um corte da img anterior.
nova_img = img[:, 0:201]
plt.imshow(nova_img)
plt.show()
print()

