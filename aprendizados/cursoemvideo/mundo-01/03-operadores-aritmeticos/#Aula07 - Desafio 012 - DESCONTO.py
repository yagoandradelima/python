#Aula07 - Desafio 012

print('=='*25)
print('=='*10, 'LIQUIDAÇÃO', '=='*10)
print('=='*25)
val = float(input('Digite o preço do produto a ser descontado: '))
calc = val * 0.05
desco = val - calc
print('=='*25)
print(f'O valor do produto era: R$ {val:.2f}')
print(f'O desconto no valor foi de: R$ {calc:.2f}')
print(f'O valor final do produto é: R$ {desco:.2f}')
print('=='*25)
print('FIM DO PROGRAMA')