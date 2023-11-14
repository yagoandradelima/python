#Aula10 - Desafio 034 - CALCULANDO SALÁRIOS

sal = float(input('Digite seu salário: '))

if sal <= 1250:
    mult = sal * 0.15
    aumento = sal + mult
    print(f'Seu salário tem um valor de R$ {sal:.2f}. O seu aumento foi de R$ {mult:.2f} e o total geral do seu salário é R$ {aumento:.2f}')

else:
    mult = sal * 0.10
    aumento = sal + mult
    print(f'Seu salário tem um valor de R$ {sal:.2f}. O seu aumento foi de R${mult:.2f} e o total geral do seu salário é R$ {aumento:.2f}')

print()
print('Fim do Programa')
