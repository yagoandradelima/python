#Aula 07 - Desafio 008

print('=='*31)
print('=='*10, 'CONVERSOR DE MEDIDAS', '=='*10)
print('=='*31)
num = float(input('Digite o valor da medida em metros: '))
mm = num*1000
cm = num*100
print('=='*31)
print(f'A medida em METROS digitada foi: {num:.3f}m')
print(f'Equivalente a {cm:<6.3f}cm e {mm:<6.4f}mm')
print('=='*31)
print('Fim')