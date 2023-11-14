#Aula12 - Desafio 041 - CLASSIFICANDO ATLETAS

from datetime import date

anoNasci = int(input('Digite o ano de nascimento do atleta: '))

idade = date.today().year - anoNasci
print()
if idade <= 9:
    print('A categoria do atleta é MIRIM!')

elif idade > 9 and idade <= 14:
    print('A categoria do atleta é INFANTIL!')

elif idade > 14 and idade <= 20:
    print('A categoria do atleta é SÊNIO')

else:
    print('A categoria do atleta é MASTER!')
print()
print('Fim do Programa')
