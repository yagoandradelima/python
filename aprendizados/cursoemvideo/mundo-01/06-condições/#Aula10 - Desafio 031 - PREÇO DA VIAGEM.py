#Aula10 - Desafio 031 - PREÇO DA VIAGEM

#No código do exercício ele remover o print dentro das condicionais e colocou no final
#Isso pois tecnicamente as condicionais podem passar o preço da passagem para o print final sem precisar existir duas delas

dist = float(input('Digite a distância da viagem: '))


if dist <= 200:
    preco = dist * 0.5
    print(f'Sua viagem será de {dist}KM e será cobrada a taxa de R$ {preco:.2f}.')

else:
    preco = dist * 0.45
    print(f'Sua viagem será de {dist}KM e será cobrada a taxa de R$ {preco:.2f}.')

print()
print('Fim do Programa')
