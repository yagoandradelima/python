#Aula07 - Desafio 014

print('=='*33)
print('=='*10, 'CONVERSOR DE TEMPERATURA', '=='*10)
print('=='*33)
temp = float(input('Digite a temperatura em ºC: '))
conv = (temp * 1.8) + 32
print('=='*31)
print(f'A temperatura digitada foi de {temp}ºC. O mesmo que {conv:.2f}ºF')
print('=='*31)
print('Final do programa')