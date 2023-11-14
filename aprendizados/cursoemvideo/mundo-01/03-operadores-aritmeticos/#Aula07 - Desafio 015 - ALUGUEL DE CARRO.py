#Aula07 - Desafio 015 - ALUGUEL DE CARROS

print('=='*33)
print('=='*10, 'ALUGUEL DE CARROS', '=='*10)
print('=='*33)
km = float(input('O carro foi utilizado por quantos KMs? '))
dias  = int(input('O carro foi alugado por quantos dias? '))
valorCarro = 60 * dias
#Escrita de variável horrorosa, jamais repetir isso
valorKm = 0.15 * km
total = valorCarro + valorKm
print('=='*33)
print(f'O carro foi utilizado por {dias} dias e rodou {km}KM(s)')
print(f'O valor total por dia utilizado foi de R$ {valorCarro}')
print(f'O valor total por KM rodado foi de R$ {valorKm}')
print('=='*33)
print(f'O valor total do seu pedido foi de R$ {total}')
print('=='*33)
print('Fim do programa')


