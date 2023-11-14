#Aula012 - Desafio 043 - CALCULANDO IMC
#Dá pra simplificar essas condições, só olhar nas atividades
from math import pow

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / pow(altura, 2)
print(f'O valor do seu imc é {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso')

elif imc > 18.5 and imc <=25:
    print('Você está no peso ideal!')

elif imc > 25 and imc <=30:
    print('Você está no estado de sobrepeso')

elif imc > 30 and imc <=40:
    print('Você está com obesidade nível 1')

else:
    print('Você possui obesidade mórbida')
    