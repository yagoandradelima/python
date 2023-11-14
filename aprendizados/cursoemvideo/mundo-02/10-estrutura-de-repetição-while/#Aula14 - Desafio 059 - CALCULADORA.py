#Aula14 - Desafio 059

#No código final ele colocou o MENU dentro do While pra ficar repetindo
#No meu código, soma e prpduto viraram op de operação. Como não há possibilidade de soma e produto serem acessados ao mesmo tempo, coloquei ambos dentro de uma variável

print('-='*10)
print("""MENU DE CALCULADORA

[ 1 ] SOMA
[ 2 ] SUBTRAÇÃO
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
""")
print('-='*10)
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

continua = 's'

while continua in 'Ss':
    esc = int(input('O que deseja fazer? '))
    print()
    if esc == 1:
        print('VOCÊ ESCOLHEU REALIZAR UMA SOMA DOS DOIS VALORES')
        op = num1 + num2
        print(f'{num1} + {num2} = {op}')
        print()
        continua = str(input('Deseja continuar? ')).strip()[0]
    
    elif esc == 2:
        print('VOCÊ ESCOLHEU REALIZAR UMA MULTIPLICAÇÃO DOS DOIS VALORES')
        op = num1 * num2
        print(f'{num1} * {num2} = {op}')
        print()
        continua = str(input('Deseja continuar? ')).strip()[0]

    elif esc == 3:
        if num1 > num2:
            print('O PRIMEIRO NÚMERO DIGITADO É MAIOR QUE O SEGUNDO')
            print()
            continua = str(input('Deseja continuar? ')).strip()[0]
        
        else:
            print('O SEGUNDO NÚMERO DIGITADO É MAIOR QUE O PRIMEIRO')
            print()
            continua = str(input('Deseja continuar? ')).strip()[0]
        
    elif esc == 4:
        print('VOCÊ ESCOLHEU MODIFICAR OS DOS DOIS VALORES')
        num1 = float(input('Digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))
        print()
        continua = str(input('Deseja continuar? ')).strip()[0]

    elif esc == 5:
        print('Fim do programa')
        continua = 'n'
        

    else:
        print('O VALOR INPUTADO NÃO CONDIZ COM NENHUMA OPÃO DO MENU')
        print('POR FAVOR, TENTE NOVAMENTE')
        print()
        continua = 's'
    

    #continua = str(input('Deseja continuar? ')).strip()[0]

print('FIM DO PROGRAMA')


