#Aula15 - Desafio 071
#Meu código é diferente do dele apesar de funcionar e ter as mesmas propriedades.
#A diferença principal está na lógica interna e a secundária está no fato dele conseguir esconder os prints de cédulas = 0
contador50 = contador10 = contador20 = contador5 = contador1 = 0
print('='*35)
print(' '*12, 'BANCO YLA')
print('='*35)
valor = int(input('Qual valor deseja sacar? '))
while (valor // 50) != 0:
    valor -= 50
    contador50 += 1
while (valor // 20) != 0:
    valor -= 20
    contador20 += 1
while (valor // 10) != 0:
    valor -= 10
    contador10 += 1
while (valor // 5) != 0:
    valor -= 5
    contador5 += 1
while (valor // 1) != 0:
    valor -= 1
    contador1 += 1
print('='*35)
#print(f'{contador100}')
print(f'Total de {contador50} cédulas de R$50')
print(f'Total de {contador20} cédulas de R$20')
print(f'Total de {contador10} cédulas de R$10')
print(f'Total de {contador5} cédulas de R$5')
print(f'Total de {contador1} cédulas de R$2')
print('='*35)
print("Volte SEMPRE! Tenha um ótimo dia!!")
