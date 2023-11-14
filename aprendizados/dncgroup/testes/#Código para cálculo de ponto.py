
continua = 's'
difEntrada = 0
somaFinal = 0
somaEntrada = 0
somaSaída = 0

while continua == 's':
    entrada = float(input('Qual seu horário de entrada? '))
    saída = float(input('Qual seu horário de saída? '))
    difEntrada = 9 - entrada
    difSaída = saída - 19
    somaEntrada += difEntrada
    somaSaída += difSaída
    continua = input('Deseja continuar [s/n]? ')
somaFinal = somaSaída + somaEntrada
print('{:.2f}'.format(somaFinal))
print()
print('Fim do programa')

