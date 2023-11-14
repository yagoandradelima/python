#Aula13 - Desafio 050

a = 0

for i in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        a +=num
print(f'A somatória total dos números digitados é: {a}')