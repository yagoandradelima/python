#Aula07 - Desafio 011

print('=='*31)
print('=='*10, 'CALCULO DE ÁREA', '=='*10)
print('=='*31)
alt = float(input('Informa a altura da sua parede: '))
lar = float(input('Informe a largura da sua parede: '))
ar = alt * lar
tin = ar//2
print('=='*31)
print(f'A altura da prede informada foi de {alt:.2f}m')
print(f'A largura da parede informada foi de {lar:.2f}m')
print(f'A área da parede é: {ar:.2f}m')
print(f'Você vai precisar de {tin} baldes de tinta')
print('=='*31)
print('Fim')