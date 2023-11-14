#Q1 Cortes em um array

import numpy as np
print('Array da questão 1')
a = np.array([np.arange(0, 6, 1), 
              np.arange(10, 16, 1), 
              np.arange(20, 26, 1),
              np.arange(30, 36, 1),
              np.arange(40, 46, 1),
              np.arange(50, 56, 1)])
print(a)
print()

print('Fatiamento laranja')
print(a[0, 3:5])
print()

print('Fatiamento vermelho')
print(a[:,2])
print()

print('Fatiamento azul')
print(a[4:,4:])

print('Fatiamento verde')
print(a[2,0], a[2,2], a[2,4], a[4,0], a[4,2], a[4,4])



