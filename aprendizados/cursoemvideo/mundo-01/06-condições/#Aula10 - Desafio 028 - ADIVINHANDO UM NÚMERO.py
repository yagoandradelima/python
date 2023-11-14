#Aula10 - Desafio 028 - ADIVINHANDO UM NÚMERO

from random import randint
from time import sleep
print('+-'*40)
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5, TENTE ADIVINHAR!')
print('+-'*40)

pc = randint(0, 5)
user = int(input('Adivinhe o número escolhido: '))

print('PROCESSANDO...')
sleep(2) #Cria um tempo para o PC dormir antes de executar o resto do código
print()
print(f'O número escolhido pelo computador foi {pc}!')

if user == pc:
    print()
    print('PARABÉNS!! Você acertou!!')

else:
    print()
    print('Não desanime. Tente novamente!')

print()
print('Fim do programa')