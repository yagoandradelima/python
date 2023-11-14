#Aula10 - Desafio 032 - ANO BISSEXTO

#import para poder fazer com que o 0 aponte para o ano atual
from datetime import date



ano = int(input('Digite o ano [coloque 0 para analisar o ano atual]: '))

#primeiro if é para o 0 retornar o ano atual
if ano == 0:
    ano = date.today().year
    print(ano)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano foi ou será, um ano bissexto!')

else:
    print('Esse ano não foi ou não será um ano bissexto!')

print()
print('Fim do Programa')