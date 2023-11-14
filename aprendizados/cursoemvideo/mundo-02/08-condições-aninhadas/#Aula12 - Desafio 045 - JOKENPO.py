#Aula12 - Desafio 045 - JOKENPO

from random import choice
from time import sleep

#No código da atividade ele pede pro usuário escolher um número dentro do MENU no meu eu peço pro usuário digitar

#Eu brinquei mais com o sleep pra brincar e deixar mais gamificado

#Ele fez uma lista com 3 posições e usou o randint. Eu fiz um choice aleatório em uma lista

#Eu fiz um big comando usando todas as condicionais onde eu venço de uma única vez. Fiz um little comando colocando a condicional simples de igualdade e deixei o big comando de vitória do PC embutido no else.

lista = ['Pedra','Papel','Tesoura']

print('*'*45)
print(' '*20, 'JOKENPO')
print('*'*45)
print('\033[7mVamos jogar JOKENPO. Você consegue me vencer?\033[m')
user = str(input('Pedra, Papel ou Tesoura? ')).strip().upper()
print('*'*45)
print()
print('\033[1;37;40mJO-\033[m')
sleep(1)
print('\033[1;37;40mKEN-\033[m')
sleep(1)
print('\033[1;37;40mPO!\033[m')
sleep(1)
print('Processando...')
sleep(2)
pc = choice(lista)
print(f'Eu escolhi {pc}')

if (user.upper() == 'TESOURA' and pc.upper() == 'PAPEL') or (user.upper() == 'PAPEL' and pc.upper() == 'PEDRA') or (user.upper() == 'PEDRA' and pc.upper() == 'TESOURA'):
    print()
    print('Você me venceu!')

elif user.upper() == pc.upper():
    print('Empatamos!')

else: 
    print('Eu venci!')

print('Fim do programa')



