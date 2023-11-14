#Aula12 - Desafio 037 - BASES NUMÉRICAS

#Incrementei o código aumentando as possibilidades de input do usuário

print('+'*33)
print(' '*5, '\033[1;32;40mCONVERSOR DE NUMEROS\033[m')
print('+'*33)
print(' '*13, '\033[7mMENU\033[m')
print()
print('1', '-'*22, 'Binário')
print('2', '-'*22, 'Hexadecimal')
print(f'3', '-'*22, 'Octal')
print('+'*33)

num = int(input('Digite um número: '))
choice = str(input('Digite para qual modelo você quer converter: ')).strip()
print()

#Dentro dos prints dos ifs, ele fatiou a string para ignorar os 0b,h e o.

if choice == '1' or choice.upper() == 'BINARIO' or choice.upper() == 'BINÁRIO':
    print(f'O número {num} convertido para binário é igual a: \033[7m{bin(num)[2:]}\033[m')

elif choice == '2' or choice.upper() == 'HEXADECIMAL' or choice.upper() == 'HEX':
    print(f'O número {num} convertido para Hexadecimal é igual a: \033[7m{hex(num)[2:]}\033[m')

elif choice == '3' or choice.upper() == 'OCTAL' or choice.upper() == 'OCTA':
    print(f'O número {num} convertido para Octal é igual a: \033[7m{oct(num)[2:]}\033[m')

else:
    print('Não entendi o que foi digitado. Por favor, tente novamente.')
print()
print('Fim do Programa')
