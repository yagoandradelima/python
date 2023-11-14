#Aula15 - Desafio 067
while True:
    num = int(input('Digite um número: '))
    print('-'*25)
    if num > 0:
        for i in range (1, 11):
            mult = num * i
            print(f'{num} x {i} = {mult}')
        print('-'*25)
    else:
        break
print('Fim do programa')