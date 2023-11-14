#Aula10 - Desafio 029 - VERIFICANDO VELOCIDADE


from time import sleep

#No código do exercício ele usou apenas uma condição para multa
#Caso o carro estivesse em velocidade normal ele iria direto para o fim do programa

print('!'*30)
print(' '*6,'RADAR ELETRÔNICO')
print('!'*30)

vel = float(input('Digite a velocidade do veículo: '))
print()

print('PROCESSANDO...')
sleep(3)
print()
multa = (vel - 80) * 7

if vel <= 80:
    print('O Carro está em velocidade permitida.')

else:
    print('O Carro está acima da velocidade permitida!')
    print(f'Uma multa de R$ {multa:.2f} deverá ser aplicada!')
print()    
print('Fim do programa')