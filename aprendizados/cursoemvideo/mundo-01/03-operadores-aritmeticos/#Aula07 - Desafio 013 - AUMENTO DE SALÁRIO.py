#Aula07 - Desafio 013

print('=='*25)
print('=='*10, 'SALÁRIO', '=='*10)
print('=='*25)
val = float(input('Digite o seu salário atual: '))
calc = val * 0.15
desco = val + calc
print('=='*25)
print(f'O valor do salário era: R$ {val:.2f}')
print(f'O aumento no valor foi de: R$ {calc:.2f}')
print(f'O seu salário final é: R$ {desco:.2f}')
print('=='*25)
print('FIM DO PROGRAMA')