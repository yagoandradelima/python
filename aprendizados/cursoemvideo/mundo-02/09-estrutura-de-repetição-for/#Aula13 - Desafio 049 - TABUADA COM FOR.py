#Aula13 - Desafio 049

print('='*33)
print('='*8, 'TABUADA NUMÉRICA', '='*7)
print('='*33)
num = int(input('Digite o número para ver a tabuada: '))

for i in range(1, 11):
    mult = i * num
    print (f'{num} X {i:2>} = {mult:5<}')
print('='*33)
print('\033[7mFIM DO PROGRAMA\033[m')
