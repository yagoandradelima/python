#Aula13 - Desafio 054

from datetime import date


contMaior = 0
contMenor = 0

for i in range(0, 7):
    nascimento = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    idade = date.today().year - nascimento

    if idade >= 21:
        contMaior += 1
    
    else:
        contMenor += 1
print()
print(f'Ao total do que foi digitado, existem {contMaior} pessoa(s) maiores de idade e {contMenor} pessoa(s) menores de idade.')

print()
print('Fim do Programa')