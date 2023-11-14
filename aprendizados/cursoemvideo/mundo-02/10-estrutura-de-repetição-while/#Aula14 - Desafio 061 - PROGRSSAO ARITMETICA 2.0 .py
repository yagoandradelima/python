#Aula14 - Desafio 061

c = 1
num = int(input('Quando o número que deseja aplicar? '))

razao = int(input('Qual o valor da razão? '))
print(f'PROGRESSÃO ARITMETICA DE {num} EM UMA RAZAO DE {razao}')

while c < 10:
    print(f'{num}', end='')
    c +=1
    print(' -> ' if c < 10 else ' = ', end='')
    num += razao
   
print(num, end='')
print()
print('Fim do programa')