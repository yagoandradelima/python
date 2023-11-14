import numpy as np

#Atividade 1. Criar uma matriz uni, bi e tridimensional.
print('Matriz unidimensional')
a = np.array(np.arange(0, 5, 1))
print(a)
print()

print('Matriz bidimensional')
b = np.array([np.arange(0, 5, 1), np.arange(0, 5 ,1)])
print(b)
print()

print('Matriz tridimensional')
c = np.array([np.arange(0 , 5, 1), np.arange(0, 5, 1), np.arange(0, 5, 1)])
print(c)
print()


#Atividade 2. Matriz identidade 5x5.
print("Matriz identidade 5x5")
d = np.eye(5)
print(d)
print()


#Atividade 3. Matriz 3x3 de 1's
print('Matriz 3x3 de 1')
e = np.ones((3, 3))
print(e)
print()


#Atividade 4. Matriz 2x3 com elementos aleatórios de 0 a 1.
print('Matriz de números aleatórios')
f = np.random.rand(2, 3)
print(f)
print()

#Atividade 5. Vetor de 10 a 0 invertido.
print('Vetor invertido')
g = np.array(np.arange(9, -1, -1))
print(g)
print()