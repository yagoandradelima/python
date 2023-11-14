import numpy as np
import matplotlib.pyplot as plt

#Q1.
#Fazendo a array par:
ap = np.arange(0, 9, 2)
#Fazendo a array ímpar
ai = np.arange(1, 10, 2)

print('Array par')
print(ap)
print()

print('Array ímpar')
print(ai)
print()

print('Soma')
print(ap+ai)
print()
print('Subtração')
print(ap-ai)
print()
print('Multiplicação')
print(ap*ai)
print()
print('Divisão')
print(ap/ai)
print()


#Q3
#A matriz deve ser produzida à mão
print('Matriz produzida à mão para atividade')
m1 = np.array([[2, 45, 22, 12], [44, 34, 68, 3],[5, 7, 78, 2], [12, 34, 5, 9]])
print(m1)
print()

#Seno da matriz
print('Seno da segunda linha da matriz')
print(np.sin(m1[1,:])) 
print()

print('Inverso da Matriz')
print(np.linalg.inv(m1))
print()
