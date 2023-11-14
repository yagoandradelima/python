#Aula12 - Desafio 039 - ANO DE NASCIMENTO
#tive que importar o ano do sistema
from datetime import date

print('+'*33)
print(' '*7, '\033[1;37;40mANO DE NASCIMENTO\033[m')
print('+'*33)

anoNasc = int(input('Digite o ano de nascimento da pessoa: '))

idade = date.today().year - anoNasc
print()
if idade == 18:
    print('Se aliste no exército! Prepare as documentações!')

elif idade > 18:
    extra = idade - 18
    print(f'Vá para o alistamento imeditamente. Você está atrasado no período de {extra} anos')

else:
    extra = 18 - idade
    print(f'Não se preocupe, ainda faltam {extra} anos para se alistar no exército.')

print()
print('Fim do programa')