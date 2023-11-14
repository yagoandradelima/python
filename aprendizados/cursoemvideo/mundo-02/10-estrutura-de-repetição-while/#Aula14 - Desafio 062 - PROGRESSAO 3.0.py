#Aula14 - Desafio 062

#nomeando contador
c = 0
termos = 1
#declarando variáveis
num = int(input('Quando o número que deseja aplicar? '))
num1 = num
razao = int(input('Qual o valor da razão? '))

print(f'PROGRESSÃO ARITMETICA DE {num} EM UMA RAZAO DE {razao}')

#bloco while
while termos != 0:
    for c in range(1, 10 + termos + 1) :
        print(f'{num}', end='')
        print(' -> ' if c < 10 else ' <- ', end='')
        num += razao
    num = num1
    termos = int(input(' \n Qual a quantidade de termos que você deseja acrescentar? '))
    

print('fim do programa')
print()
print('Fim do programa')