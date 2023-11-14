#Aula 08 - Desafio 018 - LENDO UM ÂNGULO

from math import radians, sin, cos, tan

ang = int(input('Digite o ângulo: '))
#As funções _sin_ e _cos_ para funcionar perfeitamente precisam ter a variável de cálculo convertida para radianos
seno = sin(radians(ang))
coss = cos(radians(ang))
tg = tan(radians(ang))

print(f'O seno de {ang} é {seno:.2f}. O cosseno é {coss:.2f}. E a tangente {tg:.2f}')