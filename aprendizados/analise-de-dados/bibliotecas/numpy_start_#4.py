import numpy as np
import matplotlib.pyplot as plt

#Importante lembrar que o método array possui métodos internos
#funciona com matrizes também
#favor lembrar que nesse código tem uma variável "array"
array = np.random.randn(10) #array com 10 elementos aleatórios -SHAPE (1,0)-
print(array)
print()

mtx = np.random.randn(3,2) #array com shape (3,2)
print(mtx)
print()

#retorna a dimensão do array
print(array.ndim)
print()

#retorna o shape do array
print(array.shape)
print()

#retorna o tipo de dado do array ou matriz
print(mtx.dtype) #float64 é padrão
print()

#mudando o tipo de dado do array ou matriz
print(mtx.astype('int'))#colocar o tipo de dado que quero dentro do parenteses e aspas
print(array.astype('bool'))
print()

#pegando o valor mínimo e máximo do array
print(array.min(), array.max())
print()

#posição dos elementos de um array
print(array.argmin(), array.argmax())
print()

#média do array
print(array.mean())
print()

#variancia do array
print(array.var())
print()

#desvio padrão dos elementos
print(array.std())
print()

#ordenando um array em ordem crescente
#o sort não mostra nada no output
#para entender a mudança, você deve printar novamente a variável array utilizada
print(array.sort())
print(array)
print()

#calculando a transposta de uma matriz
print(mtx.T)
print()

#Máscara são arrays de booleanos (TRUE, FALSE) que indicam se minha solicitação é VERDADEIRA ou FALSA
#com relação a outro array
a = np.array([7, 8, 9, 10])
#Quero somente os elementos true
print(a[[True, False, True, True]])
print(a >= 9)
#Se eu remover o a[ ] da solicitação abaixo, ele vai me retornar TRUE ou FALSE e não os números
print (a[a%2==0])


