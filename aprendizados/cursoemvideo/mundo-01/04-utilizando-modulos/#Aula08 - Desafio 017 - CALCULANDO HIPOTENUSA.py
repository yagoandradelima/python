#Aula08 - Desafio 017
from math import hypot, sqrt

catOposto = float(input('Digite o tamanho do cateto oposto: '))
catAdj = float(input('Digite o tamanho do cateto adjacente: '))
hip = (catOposto**2) + (catAdj**2)
hipo = float(sqrt(hip))
print(f'O valor da hipotenusa é {hipo:.2f}')
print('Fim do programa')

#Abaixo, comentado, vem a solução resumida do problema da hipotenusa
#_hip = math.hypot(catOposto, catAdj)_