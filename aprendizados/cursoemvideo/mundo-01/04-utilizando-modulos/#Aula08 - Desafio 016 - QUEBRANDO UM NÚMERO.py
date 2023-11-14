#Aula08 - Desafio 016

import math

num = float(input('Digite um número inteiro real acima de 3 casas após a vírgula: '))
#A função trunc elimina da vírgula pra frente, deixando só a parte real
vis = math.trunc(num)
print(vis)

#O Truncate quebra o número na parte inteira. No caso desse desafio, se fosse da minha preferência
#eu poderia simplesmente ter utilizado o _int_ no lugar do truncate