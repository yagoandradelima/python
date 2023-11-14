#Aula14 - Desafio 058

from random import randint

print('-='*22)
print(' '*7, '\033[1;34;40mJOGO DE ADIVINHAÇÃO V2.0\033[m')
print('-='*22)

print('- \033[7mVOCÊ consegue adivinhar o número que escolhi?\033[m')
user = int(input('- \033[7mQual foi o número que escolhi?\033[m '))

pc = randint(0, 10)
contador = 0

while user != pc:
    print('- \033[7mVocê não acertou! Tente novamente!\033[m')
    user = int(input('- \033[7mQual foi o número que escolhi?\033[m '))
    print()
    contador += 1

    if user == 0:
        print('- \033[7mVocê não acertou! Tente novamente!\033[m')
    user = int(input('- \033[7mQual foi o número que escolhi?\033[m '))
    print()
    contador += 1

else:
    print(f'- \033[7mParabéns!! Você adivinhou!! Eu havia escolhido o número {pc}!\033[m')
print(f'- \033[7mVocê conseguiu acertar na {contador}ª escolha.\033[m')
