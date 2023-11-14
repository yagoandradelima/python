#Aula14 - Desafio 060

from os import remove


num = int(input('Digite um número: '))
num1 = num
fat = 0
mult = 1
juncao = ''

print()
while num != 0:
    #Observar esse print. O if foi usado de maneira muito inteligente
    print(f'{num}', end='')
    print(' x ' if num > 1 else ' = ', end='')
    mult *= num
    num -= 1
    
print(f'{mult}')
